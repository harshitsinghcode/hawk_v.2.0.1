from django.shortcuts import render, redirect
from app.models import Databases
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db import connection
import subprocess, shlex
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt  
from django.http import JsonResponse as JsonResponse

# Rest of your views...


# Create your views here.

def index(request):
    return render(request, "app/index.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "New user created! Please sign in.")
            return redirect('app:index')
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form":form})

@login_required
def home(request):
    return render(request, "app/home.html")

@login_required
def databases(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        department = request.POST.get("department")
        designation = request.POST.get("designation")

        # Saving to DB using Django ORM - the best way
        Databases.objects.create(emp_id=emp_id, first_name=first_name, last_name=last_name,
        age=age, sex=sex, department=department, designation=designation)

        # # Direct SQL Queries - the wrong way
        # cursor = connection.cursor()
        # query = "INSERT INTO app_databases (emp_id, first_name, last_name, age, sex, department, designation) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (emp_id, first_name, last_name, age, sex, department, designation)
        # cursor.execute(query)

        # # Direct SQL Queries - the correct way
        # cursor = connection.cursor()
        # cursor.execute("INSERT INTO app_employee (emp_id, first_name, last_name, age, sex, department, designation) VALUES (%s, %s, %s, %s, %s, %s, %s)", [emp_id, first_name, last_name, age, sex, department, designation])

        return redirect("app:databases")
    else:
        # Fetch all employees using Django ORM
        databases = Databases.objects.all()

        return render(request, 'app/databases.html', {"databases": databases})




@login_required
@csrf_exempt
def searchdb(request):
    search_term = request.POST.get('searchTerm', '')
    query = f"SELECT * FROM app_databases WHERE first_name LIKE '%s' COLLATE NOCASE;" % search_term
    databases = Databases.objects.raw(query)

    if request.method == 'POST':
        with connection.cursor() as cursor:
            ot = "DELETE FROM app_databases;"
            cursor.execute(search_term)
       
    # print(search_term)
    return render(request, 'app/searchdb.html', {'databases': databases})

def searchdb(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_term = request.POST.get('searchTerm')

        # Use __icontains for case-insensitive search
        databases = Databases.objects.filter(first_name__icontains=search_term)

        # Render a template with the filtered databases
        return render(request, 'app/searchdb.html', {'databases': databases})
    else:
        # Return an error message if it's not a valid AJAX POST request
        return render(request, 'app/databases.html', {'error_message': 'Invalid request'})
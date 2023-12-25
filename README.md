# Hawk v.2.0.1 - Django-Security Testing Website 🚀!

## Overview ❄️: 

Welcome to Hawk v.2.0.1, a testing website built on Django that focuses on security. This web application includes login functionality, database management, and a search feature. The project aims to demonstrate various security aspects in Django and the importance of using the Django ORM for protection against common vulnerabilities.

## Security Highlights 🔐:

### Common Security Risks Addressed:

1. **Cross-Site Request Forgery (CSRF) Protection**: Django's built-in protection against CSRF attacks.
2. **Cross-Site Scripting (XSS) Protection**: Secure handling of user input to prevent XSS vulnerabilities.
3. **SQL Injection Prevention**: The use of Django ORM prevents SQL injection vulnerabilities.
4. **Clickjacking Prevention**: Protection against Clickjacking attacks.
5. **SSL/HTTPS**: Encrypted communication for enhanced security.

### SQL Injection Example 💉:

- **Vulnerability**: Allows a malicious user to execute arbitrary SQL code.
- **Django Security Measure**: Query parameterization and the use of Django ORM to prevent SQL injection.

## Installation 🛠️:

- Follow the steps below to set up the project locally:

  ```bash
  git clone https://github.com/harshitsinghcode/hawk_v.2.0.1.git
  cd hawk_v.2.0.1
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver

## Contributing 🤝:

I welcome contributions from the community to make Hawk v.2.0.1 even more secure and feature-rich. To contribute:

- Fork the repository.
- Create a new branch.
- Make your changes.
- Submit a pull request.
- Read the Contribution Guide for more details.

## License 📝:

This project is licensed under the MOZILLA PUBLIC LICENSE - see the LICENSE file for details.
Happy testing and coding🎅🏻✨!


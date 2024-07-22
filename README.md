Description
This project is a customer and order management system built with Django. It includes user authentication using OIDC, customer registration, order creation, and searching for orders within a specified date range. The project also integrates with Django Rest Framework (DRF) to provide API endpoints for managing customers and orders.

Features
User Authentication with OIDC
Customer Registration
Order Creation
Search Orders by Date Range
REST API for Customers and Orders
Responsive Design with Bootstrap
Unit Tests with Coverage Reporting
CI/CD Setup
Setup
Prerequisites
Python 3.x
Django 4.x
Django Rest Framework
Bootstrap 4.x

Installation
Clone the repository:

bash
git clone https://github.com/Jefe614/Django-OIDC-.git
cd Django-OIDC
Create a virtual environment and activate it:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
pip install -r requirements.txt
Apply the migrations:

bash
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
python manage.py createsuperuser
Run the development server:

bash
python manage.py runserver
Running the Application
Access the application at http://127.0.0.1:8000/.
Log in with the superuser credentials created earlier.
Register new customers and create orders.
Use the search functionality to find orders within a specified date range.
Running Tests
To run the unit tests with coverage reporting:

Install coverage if not already installed:

bash
pip install coverage
Run the tests:

bash
coverage run manage.py test
Generate the coverage report:

bash
coverage report

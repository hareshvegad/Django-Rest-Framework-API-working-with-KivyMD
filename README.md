Django Rest Framework API working with KivyMD

Frontend application using KivyMD in Python and a backend application using Django. The purpose of the code is to create a CRUD (Create, Read, Update, Delete) interface for managing student data.

Here's a brief overview of the code:
Frontend (KivyMD):

    The frontend application is built using the KivyMD framework for the UI.
    It consists of a simple interface with text fields for entering student ID, name, roll, and city.
    There are buttons for performing CRUD operations: GET, POST, UPDATE, and DELETE.
    Each button triggers a corresponding method (get_data, post_data, update_data, delete_data), which makes API requests to the Django backend.

Backend (Django):

    The backend uses Django as the web framework.
    It defines a Student model with fields for name, roll, and city.
    The views.py file contains a StudentApi class that inherits from viewsets.ModelViewSet, providing CRUD operations for the Student model.
    URLs are configured using a router to map the StudentApi viewset to appropriate endpoints.

Suggestions:

    Ensure that your Django development server is running (python manage.py runserver).
    Make sure the Django models are migrated (python manage.py makemigrations and python manage.py migrate).
    Test your API endpoints using tools like Postman or by accessing them through a browser.
    Run your KivyMD application and check if it successfully communicates with the Django backend.

It's important to note that for this code to work, both the frontend and backend need to be running concurrently. Additionally, you need to replace http://127.0.0.1:8000/ with the appropriate address where your Django development server is running.
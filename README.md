# ForumBackend

Simple forum Django REST API to list and create posts and comments.

## Requirements:
* Django==3.1.1
* django-cors-headers==3.5.0
* djangorestframework==3.11.1

## Setup:
* Initialize your favorite Python virtual enviroment
* Install requirements: ```pip install -r requirements.txt```
* Migrate Data Model to the database:
  * ```python manage.py makemigrations posts```
  * ```python manage.py migrate posts```
* Run the Django Project with command: ```python manage.py runserver 8080```



### Postman Documentation: 
https://documenter.getpostman.com/view/12620310/TVCiSR7W#64f62596-6903-4d23-88e0-63837f8ed5ca


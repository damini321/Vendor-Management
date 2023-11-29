# Vendor-Management

*Github
-Create new git repository.
-Clone the required git submodules.

*Create New Project
 ```
  django-admin startproject vendor_management_system
  ```

*Create App
```
python manage.py startapp vendor_management
```
*Added app in settings.py file and install restframework packange
```
'rest_framework',
'vendor_management',

```
*Added Vendor & Purchase Order Models
* Makemigrations and Migrate the code
* Create superuser for admin panel
* run the code

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser 
python manage.py runserver

```

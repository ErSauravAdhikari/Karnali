
# Karnali

Karnali is a demo app I created while learning how to use the Django Ninja Rest API framework.

It's a straightforward app with two models for books and chapters. A book is referenced in each chapter.

I spent around 3–4 hours learning this new framework, and here is the sample app I created as a consequence.

Please do not use this code in any production situations, despite the fact that I feel I do not need to mention it. This app will not be updated, and no new features will be added.


## Lessons Learned

- Building REST APIs in Django 
- Django Ninja Rest Framework
- Adding authentication in Django Ninja API [Cookie Based]
- Creating folder based structure for a single app

## Acknowledgements

 - [Django Project](https://www.djangoproject.com/)
 - [Django Ninja Rest Framework](https://django-ninja.rest-framework.com/)
 - [Django Ninja Authentication (Some Codes Were Referenced)](https://github.com/mugartec/django-ninja-auth)


## Authors

- [@ErSauravAdhikari](https://www.github.com/ersauravadhikari)

## Screenshots
![image](https://user-images.githubusercontent.com/69170305/167658996-b80cb207-27f1-4cbd-9f2a-9e7c4d89548f.png)


## Run Locally

Please follow the usual Installation and execution proceduere for django based projects.

### Virtual Env Configuration[Optional]
```bash
pip3 install virtualenv
python3 -m virtualenv venv
```
#### For Linux Systems
```bash
source ./venv/bin/activate
```

### Run Locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

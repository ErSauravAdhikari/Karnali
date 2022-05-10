
# Karnali

Karnali is an example app I have built while learning to use the django ninja rest api framework. 

It is a simple app with two models for books and chapters. Each chapter referencing the book. 

I spent around 3-4 hours trying to learn this new framework and this is the example app I built as a result of that.

Although I believe I don't need to say this, however Please do not use this code in any production settings. This will not be maintained and no new features will be added in this app.


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

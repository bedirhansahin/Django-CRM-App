# DJANGO CRM APP

## Technologies I used while developing the project:


- Django
- PostgreSQL
- Django Model Form
- Bootstrap


## You Can:


- Create a new user
- Create a new customer
- Update customer
- Delete customer


## Download the project

First, create a folder and run
```
git clone https://github.com/bedirhansahin/todo-photo-app.git
cd todo-photo-app
pip3 install -r requirements.txt
```
After, Create a postgresql server, create an '.env' file and include SECRET_KEY, DB_NAME, DB_PASS, DB_USER
in it (Host: localhost and Port: 5432) and Create new schemas named django_crm_app and newschema

After, run
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

and you can go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your own browser.
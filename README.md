# a cookiecutter based on django_styleguide

https://github.com/HackSoftware/Django-Styleguide

## usage

install cookiecutter
```
pip install cookiecutter
```

setup the project
```
cookiecutter git@github.com:amirbahador-hub/django_style_guide.git
```

## project setup

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd Project_name
```

2- SetUp venv
```
virtualenv venv
source venv/bin/activate
```

3- install Dependencies
```
pip install -r requirements.txt
```

4- spin off docker compose
```
docker-compose -f docker-compose.dev.yml up -d
```

5- run the project
```
python manage.py runserver
```



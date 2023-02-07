# {{cookiecutter.project_name}}

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

5- create your env
```
cp .env.example .env
```

6- Create tables
```
python manage.py migrate
```

7- run the project
```
python manage.py runserver
```



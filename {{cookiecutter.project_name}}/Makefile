start-dev:
	@virtualenv -p python3.10 venv
	@source venv/bin/activate 
	@pip install -r requirements_dev.txt
	@pip install -r requirements.txt
	@cp .env.example .env
	@python manage.py migrate
	@python manage.py runserver
dev-on:
	@docker compose -f docker-compose.dev.yml up -d
	@python manage.py runserver
dev-off:
	@docker compose down

migrate:
	@python manage.py makemigrations
	@python manage.py migrate
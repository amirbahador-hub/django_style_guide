echo "--> Starting beats process"
celery -A {{cookiecutter.project_slug}}.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

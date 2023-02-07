echo "--> Starting celery process"
celery -A embed.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

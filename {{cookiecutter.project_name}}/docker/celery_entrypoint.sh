echo "--> Starting celery process"
celery -A {{cookiecutter.project_slug}}.tasks worker -l info --without-gossip --without-mingle --without-heartbeat

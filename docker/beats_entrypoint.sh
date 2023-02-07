echo "--> Starting beats process"
celery -A embed.tasks worker -l info --without-gossip --without-mingle --without-heartbeat

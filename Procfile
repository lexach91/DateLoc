release: python manage.py migrate
web: daphne DateLoc.asgi:application
worker: python manage.py runworker -v2 channel_layer
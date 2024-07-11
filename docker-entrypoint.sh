#!/bin/sh

apply_migrations() {
  echo "Applying database migrations..."
  poetry run python manage.py migrate
}

start_dev_server() {
  echo "Starting the development server..."
  poetry run python manage.py runserver 0.0.0.0:8000
}

start_prod_server() {
  echo "Starting the Gunicorn server..."
  poetry run gunicorn -c backend/guniconf.py backend.wsgi:application
}

case "$1" in
  dev)
    apply_migrations
    start_dev_server
    ;;
  prod)
    apply_migrations
    start_prod_server
    ;;
  *)
    echo "Usage: $0 {dev|prod}"
    exit 1
    ;;
esac

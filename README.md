# book_shop
Command to start project:
  docker-compose-v1 up -d --build
  docker-compose-v1 exec shop python manage.py migrate --noinput
  
  

env file example:
  DEBUG=1
  DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
  SQL_ENGINE=django.db.backends.postgresql
  SQL_DATABASE=...
  SQL_USER=...
  SQL_PASSWORD=...

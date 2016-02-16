web: uwsgi --lazy --http-socket :$PORT --module agileteamskpisapi.wsgi -L -p 4  -l 128 --check-static collected_static --static-map /static=collected_static

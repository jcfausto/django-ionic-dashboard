#web: gunicorn agileteamskpisapi.wsgi --log-file -
#web: uwsgi --lazy --http-socket :8000 --module agileteamskpisapi.wsgi -L -p 4  -l 128 --static-map /lib=/collected_static/lib
#web: uwsgi --lazy --http-socket :$PORT --module agileteamskpisapi.wsgi -L -p 4  -l 128 --check-static collected_static --static-map /static=collected_static
web: uwsgi --lazy --http-socket :$PORT --module agileteamskpisapi.wsgi -L -p 4  -l 128 --check-static collected_static --static-map /static=./collected_static --static-map /lib=./collected_static/lib

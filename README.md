# Django Ionic Dashboard

This is a django rest framework api and an IONIC app able to run on heroku or dokku.

# Live demo here:

https://didashboard.herokuapp.com

# To deploy to heroku

```bash
$ heroku create mydashboard
$ git push heroku master
$ heroku config:set DJANGO_SETTINGS_MODULE=agileteamskpisapi.settings
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku ps:scale web=1
```

- Login with the admin credentials into the API https://mydashboard.herokuapp.com/api/ and fill some data.
- The dashboard runs at https://mydashboard.herokuapp.com




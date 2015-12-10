# django-uwsgi-nginx
Example of a Django site served by uWSGI and nginx.

Implements a simple "Hello, world!", but with a few extras (templates, CSS, 
images, etc.).

Installation steps on Debian 8
------------------------------

- Install nginx as system-wide service.

    apt-get update && apt-get upgrade
    apt-get install nginx

- Install uWSGI as system-wide service.

    apt-get install uwsgi

- `git clone` this repo, for example in `/var/www`. Note: if you choose a different
location, change `nginx.conf` and `uwsgi.ini` accordingly.

    cd /var/www
    git clone https://github.com/nicodv/django-uwsgi-nginx.git

- Create a virtualenv with latest `pip`, `setuptools`, and `django` packages,
for example in `/var/www/djangsite/venv`. Note: if you choose a different location,
change `uwsgi.ini` accordingly.

- Determine the version of Python you are using and edit `uwsgi.ini` accordingly.

- Remove `nginx` default site config and make a symbolic link to the `nginx.conf`
file in the `/etc/nginx/conf.d` directory.

    rm /etc/nginx/sites-enabled/default
    ln -s /var/www/djangosite/conf/nginx.conf /etc/nginx/conf.d/
    service nginx restart

- Make symbolic links of the `uwsgi.ini` file to the `/etc/uwsgi/apps-available` 
and `/etc/uwsgi/apps-enabled` directories.

    ln -s /var/www/djangosite/conf/uwsgi.ini /etc/uwsgi/apps-available/
    ln -s /var/www/djangosite/conf/uwsgi.ini /etc/uwsgi/apps-enabled/

- Hack the `uwsgi` service to use the so-called emperor, which will automatically
serve any `.ini` file in `/etc/uwsgi/apps-enabled`.

    service uwsgi restart

- Create the log directories.

    mkdir -p /var/log/uwsgi

- Set permissions correctly for user `www-data`. Note: if you run as a different
user, change `/etc/nginx/nginx.conf`, `uwsgi.ini`, and these commands accordingly.

    chown -R www-data:www-data /var/www/djangosite/
    chmod www-data:www-data /var/log/uwsgi/
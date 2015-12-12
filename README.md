# django-uwsgi-nginx
Example of a Django site served by uWSGI and nginx for testing and education purposes.

Implements a simple "Hello, world!", but with a few extras (templates, CSS, 
images, etc.).

**Warning: this example is not suitable for production and should be considered insecure (e.g., the `SECRET_KEY` is currently hardcoded in `settings.py`)!**

Installation steps on Debian 8
------------------------------

- Install nginx and uWSGI as system-wide services.

    ```
    apt-get update && apt-get upgrade
    apt-get install nginx
    apt-get install uwsgi
    ```

- `git clone` this repo, for example in `/var/www`. Note: if you choose a different
location, change `nginx.conf` and `uwsgi.ini` accordingly after cloning.

    ```
    cd /var/www
    git clone https://github.com/nicodv/django-uwsgi-nginx.git
    ```

- Create a virtualenv with the latest `pip`, `setuptools`, and `django` packages,
for example in `/var/www/django-uwsgi-nginx/venv`. Note: if you choose a different
location, change `uwsgi.ini` accordingly.

- Install the Python plugin to uWSGI. Note: I assume Python 3 here. The Python 2
command is the same, minus the `3`. Also, if you're using Python 2, edit
`uwsgi.ini` accordingly by editing the plugin name.

    ```
    apt-get install uwsgi-plugin-python3
    ```

- Remove nginx's default site config and make a symbolic link to the
`nginx.conf` file in the `/etc/nginx/conf.d` directory.

    ```
    rm /etc/nginx/sites-enabled/default
    ln -s /var/www/django-uwsgi-nginx/conf/nginx.conf /etc/nginx/conf.d/
    service nginx restart
    ```

- Make symbolic links of the `uwsgi.ini` file to the `/etc/uwsgi/apps-available` 
and `/etc/uwsgi/apps-enabled` directories.

    ```
    ln -s /var/www/django-uwsgi-nginx/conf/uwsgi.ini /etc/uwsgi/apps-available/
    ln -s /var/www/django-uwsgi-nginx/conf/uwsgi.ini /etc/uwsgi/apps-enabled/
    ```

- Hack the `uwsgi` service to use the so-called emperor, which will automatically
serve any `.ini` file in `/etc/uwsgi/apps-enabled`. Do this by editing
`/etc/init.d/uwsgi` and adding `--emperor /etc/uwsgi/apps-enabled` after the
service start command so that it reads
`"Starting $DESC" "$NAME" --emperor /etc/uwsgi/apps-enabled`). Then reload and
restart the service:

    ```
    systemctl daemon-reload
    service uwsgi restart
    ```

- Create the log directories.

    ```
    mkdir -p /var/log/uwsgi
    ```

- Set permissions correctly for user `www-data`. Note: if you run as a different
user, change `/etc/nginx/nginx.conf`, `uwsgi.ini`, and these commands accordingly.

    ```
    chown -R www-data:www-data /var/www/django-uwsgi-nginx/
    chown www-data:www-data /var/log/uwsgi/
    ```
- Check it out!

    ```
    http://<your.ip.add.ress>/helloworld/
    ```

Debugging
---------
nginx logs can be found in `/var/log/nginx`, and uWSGI logs in `/var/log/uwsgi`.
You can also try to run the uWSGI server manually with:

    uwsgi --ini /var/www/django-uwsgi-nginx/conf/uwsgi.ini

To do
-----
- Enhance security

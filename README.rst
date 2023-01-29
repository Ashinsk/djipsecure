=====
Django IP Secure
=====

Djipsecure is a Django app which helps to secure requests with only allowed IPs.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'djipsecure',
    ]

2. Run ``python manage.py migrate`` to create the djipsecure models.

3. Start the development server and visit http://127.0.0.1:8000/admin/

4. Visit http://127.0.0.1:8000/admin/djipsecure/useripaddress/ to allow user IPs.

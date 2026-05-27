"""
WSGI config for my_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

application = get_wsgi_application()

# Run pending migrations at startup so Render and other deploy targets can create the database schema automatically.
# This is safe for simple deployments and avoids "no such table" errors when the SQLite database is empty.
if os.environ.get('AUTO_MIGRATE_ON_STARTUP', '1') == '1':
    try:
        from django.core.management import call_command

        call_command('migrate', interactive=False)
    except Exception:
        pass

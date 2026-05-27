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

    try:
        from django.contrib.auth import get_user_model
        from main.models import Module, Topic, Presentation, TopicImage
        from original_views import MODULES

        User = get_user_model()
        admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'Admin1234')
        admin_email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')

        if not User.objects.filter(username=admin_username, is_superuser=True).exists():
            User.objects.create_superuser(admin_username, admin_email, admin_password)

        if Module.objects.count() == 0:
            for module_data in MODULES:
                module = Module.objects.create(
                    title=module_data['title'],
                    description=module_data.get('description', ''),
                    order=module_data.get('id', 0),
                    info=module_data.get('info', ''),
                )
                for topic_data in module_data.get('topics', []):
                    topic = Topic.objects.create(
                        module=module,
                        title=topic_data['title'],
                        description=topic_data.get('description', ''),
                        order=topic_data.get('id', 0),
                        info=topic_data.get('info', ''),
                    )
                    for pres_data in topic_data.get('presentations', []):
                        Presentation.objects.create(
                            topic=topic,
                            title=pres_data.get('title', ''),
                            file=None,
                            order=0,
                        )
                    for img_data in topic_data.get('images', []):
                        TopicImage.objects.create(
                            topic=topic,
                            caption=img_data.get('caption', ''),
                            image=None,
                            order=0,
                        )
    except Exception:
        pass

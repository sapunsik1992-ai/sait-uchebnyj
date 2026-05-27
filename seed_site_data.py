import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from main.models import Module, Topic, Presentation, TopicImage
from original_views import MODULES

Module.objects.all().delete()
Topic.objects.all().delete()
Presentation.objects.all().delete()
TopicImage.objects.all().delete()

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

print('Site modules restored from original_views.py')

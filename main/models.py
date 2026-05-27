from django.db import models


class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    icon = models.ImageField(upload_to='module_icons/', blank=True, null=True)
    header_image = models.ImageField(upload_to='module_headers/', blank=True, null=True)
    info = models.TextField(blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return self.title


class Topic(models.Model):
    module = models.ForeignKey(Module, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    info = models.TextField(blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return f'{self.module.title} — {self.title}'


class Presentation(models.Model):
    topic = models.ForeignKey(Topic, related_name='presentations', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='presentations/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'

    def __str__(self):
        return self.title


class TopicImage(models.Model):
    topic = models.ForeignKey(Topic, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='topic_images/', blank=True, null=True)
    caption = models.CharField(max_length=250, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Изображение темы'
        verbose_name_plural = 'Изображения тем'

    def __str__(self):
        return self.caption or f'Изображение для {self.topic.title}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class AssistantMessage(models.Model):
    ROLE_CHOICES = [
        ('user', 'Пользователь'),
        ('assistant', 'Помощник'),
    ]

    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение помощника'
        verbose_name_plural = 'Сообщения помощника'

    def __str__(self):
        return f'{self.get_role_display()}: {self.text[:50]}'

from pathlib import Path

path = Path(r'c:\Users\titi\Desktop\сайт учебный\main\views.py')
text = path.read_text(encoding='utf-8')
start = text.index("        'topics': [")
end = text.index("        ],\n    },\n]", start) + len("        ],\n    },\n]")
new_topics = r"""        'topics': [
            {
                'id': 1,
                'title': 'Глава 1. Введение в Django',
                'description': 'Обзор фреймворка, архитектуры MVT, установка и создание первого проекта.',
                'presentations': [
                    {
                        'title': 'Начало работы с Django',
                        'filename': '4.1._Знакомство_с_Django._Подготовка_и_запуск_проекта_1404.pdf',
                    },
                ],
                'info': '''
<h3>Что такое Django</h3>
<p>Django - это высокоуровневый Python-фреймворк для разработки веб-приложений. Он помогает быстро создавать сайты благодаря готовым компонентам: маршрутизация, ORM, система шаблонов, аутентификация и админ-панель.</p>

<h3>Архитектура MVT</h3>
<p>В Django принята архитектура <strong>MVT</strong> (Model-View-Template), где:</p>
<ul>
<li><strong>Model</strong> - описывает данные и хранится в базе данных.</li>
<li><strong>View</strong> - обрабатывает запрос и возвращает ответ.</li>
<li><strong>Template</strong> - отвечает за HTML-разметку.</li>
</ul>

<h3>Установка и создание проекта</h3>
<p>Рекомендуется использовать виртуальное окружение:</p>
<pre>python -m venv .venv
.\.venv\Scripts\Activate.ps1</pre>
<p>После активации установите Django:</p>
<pre>python -m pip install django</pre>
<p>Инициализируйте проект:</p>
<pre>django-admin startproject my_project .</pre>

<h3>Создание приложения</h3>
<p>Приложение создается командой:</p>
<pre>python manage.py startapp main</pre>
<p>Добавьте <code>main</code> в <code>INSTALLED_APPS</code> в <code>my_project/settings.py</code>.</p>
''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/django.png',
                        'caption': 'Django - мощный фреймворк для разработки веб-приложений.',
                    },
                    {
                        'src': settings.STATIC_URL + 'main/images/главная страничка.png',
                        'caption': 'Пример завершенной страницы учебного сайта.',
                    },
                ],
            },
            {
                'id': 2,
                'title': 'Глава 2. Представления и маршрутизация',
                'description': 'Как Django обрабатывает запросы и настраивает URL.',
                'presentations': [],
                'info': '''
<h3>Цикл обработки запроса</h3>
<p>Когда браузер отправляет запрос, Django выбирает view, который его обрабатывает. View получает объект <code>request</code> и возвращает ответ.</p>

<h3>URL-маршруты</h3>
<p>Маршруты настраиваются в файле <code>urls.py</code> с помощью <code>path</code> или <code>re_path</code>.</p>
<pre>from django.urls import path
from . import views

urlpatterns = [
    path('', views.module_list, name='module_list'),
    path('modules/<int:module_id>/', views.module_detail, name='module_detail'),
    path('modules/<int:module_id>/topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]
</pre>

<h3>HttpRequest и HttpResponse</h3>
<p><code>HttpRequest</code> содержит данные запроса, а <code>HttpResponse</code> отсылает результат пользователю.</p>

<h3>Параметры и формы</h3>
<p>Доступ к параметрам строки запроса через <code>request.GET</code>, к данным формы - через <code>request.POST</code>.</p>

<h3>Дополнительные ответы</h3>
<p>Можно возвращать JSON, перенаправления и статусные коды.</p>
''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/3.11.png',
                        'caption': 'Определение маршрутов и привязка views.',
                    },
                    {
                        'src': settings.STATIC_URL + 'main/images/3.12.png',
                        'caption': 'Пример маршрутизатора Django и URL-паттернов.',
                    },
                ],
            },
            {
                'id': 3,
                'title': 'Глава 3. Шаблоны и статика',
                'description': 'Создание шаблонов, передача контекста и подключение статических файлов.',
                'presentations': [],
                'info': '''
<h3>Шаблоны Django</h3>
<p>Шаблоны хранятся в папке <code>templates</code>. В них используются выражения, теги и фильтры.</p>

<h3>Передача данных</h3>
<p>Контекст передается из view в шаблон с помощью функции <code>render</code>.</p>

<h3>Статические файлы</h3>
<p>Для CSS, JavaScript и изображений применяется тег <code>{% static %}</code>.</p>
<pre>{% load static %}
<link rel="stylesheet" href="{% static 'main/site.css' %}">
</pre>

<h3>Расширение шаблонов</h3>
<p>Шаблоны можно наследовать с помощью <code>{% extends %}</code> и вставлять фрагменты через <code>{% include %}</code>.</p>
''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/3.13.png',
                        'caption': 'Шаблоны Django позволяют оформлять страницы и подключать статику.',
                    },
                    {
                        'src': settings.STATIC_URL + 'main/images/1.22.png',
                        'caption': 'Структура проекта с папками templates и static.',
                    },
                ],
            },
            {
                'id': 4,
                'title': 'Глава 4. Формы Django',
                'description': 'Определение форм, валидация и обработка POST-запросов.',
                'presentations': [],
                'info': '''
<h3>Создание форм</h3>
<p>Формы описываются на основе <code>forms.Form</code> и <code>forms.ModelForm</code>.</p>
<pre>from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
</pre>

<h3>Обработка формы</h3>
<p>Во view проверяйте метод запроса и валидность формы.</p>
<pre>if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
</pre>

<h3>Валидация</h3>
<p>Метод <code>is_valid()</code> проверяет данные, а <code>form.errors</code> содержит сообщения об ошибках.</p>
''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/1.17.png',
                        'caption': 'Формы Django и их поля.',
                    },
                    {
                        'src': settings.STATIC_URL + 'main/images/1.18.png',
                        'caption': 'Обработка пользовательских данных формы.',
                    },
                ],
            },
            {
                'id': 5,
                'title': 'Глава 5. Модели и ORM',
                'description': 'Модели, миграции, запросы и связи данных.',
                'presentations': [],
                'info': '''
<h3>Модели Django</h3>
<p>Модели описываются в <code>models.py</code> и наследуются от <code>models.Model</code>.</p>
<pre>from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
</pre>

<h3>Миграции</h3>
<p>После создания модели выполняются команды:</p>
<pre>python manage.py makemigrations
python manage.py migrate</pre>

<h3>Запросы ORM</h3>
<p>Основные операции:</p>
<ul>
<li><code>Article.objects.all()</code></li>
<li><code>Article.objects.filter(title__icontains='django')</code></li>
<li><code>Article.objects.get(pk=1)</code></li>
<li><code>Article.objects.create(...)</code></li>
</ul>

<h3>Связи</h3>
<p>Используются <code>ForeignKey</code>, <code>ManyToManyField</code> и <code>OneToOneField</code>.</p>
''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/1.19.png',
                        'caption': 'Модели Django и их поля.',
                    },
                    {
                        'src': settings.STATIC_URL + 'main/images/1.20.png',
                        'caption': 'Примеры запросов ORM и работы с базой данных.',
                    },
                ],
            },
            {
                'id': 6,
                'title': 'Глава 6. Создание сайта Django',
                'description': 'Пошаговый учебный отчет по созданию реального сайта Django.',
                'presentations': [
                    {
                        'title': 'Пошаговый учебный отчет по созданию сайта Django',
                        'filename': 'Django_Пошаговый_Отчет.pdf',
                    },
                ],
                'info': '''
<h3>Подготовка рабочего каталога</h3>
<p>Создайте папку на рабочем столе и перейдите в нее:</p>
<pre>mkdir "C:\Users\titi\Desktop\ДЖАНГО"
cd "C:\Users\titi\Desktop\ДЖАНГО"</pre>

<h3>Виртуальное окружение</h3>
<p>Создайте и активируйте виртуальное окружение:</p>
<pre>python -m venv .venv
.\.venv\Scripts\Activate.ps1</pre>

<h3>Установка зависимостей</h3>
<pre>python -m pip install --upgrade pip
python -m pip install django python-docx reportlab</pre>

<h3>Создание проекта и приложения</h3>
<p>Инициализируйте проект и приложение:</p>
<pre>django-admin startproject my_project .
python manage.py startapp main</pre>

<h3>Регистрация приложения и маршрутов</h3>
<p>Добавьте приложение в <code>INSTALLED_APPS</code> и настройте <code>urls.py</code>.</p>

<h3>Запуск сервера</h3>
<p>Проверьте, что сайт работает локально:</p>
<pre>python manage.py runserver</pre>

<h3>Деплой и сбор статики</h3>
<p>Для продакшна соберите статику и подключите <code>whitenoise</code>:</p>
<pre>python manage.py collectstatic --noinput</pre>
''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/1.21.png',
                        'caption': 'Пошаговое создание учебного сайта на Django.',
                    },
                    {
                        'src': settings.STATIC_URL + 'main/images/1.22.png',
                        'caption': 'Структура проекта Django и статических ресурсов.',
                    },
                ],
            },
        ],
    },
]"""
text = text[:start] + new_topics + text[end:]
path.write_text(text, encoding='utf-8')
print('updated topics list')

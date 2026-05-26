from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from main.models import Product

MODULES = [
    {
        'id': 1,
        'title': 'Основы языка программирования',
        'description': 'Первый модуль курса по Python. Изучите основные концепции программирования.',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Python. Знакомство с консолью',
                'description': 'Первая тема модуля. Учитесь работать с интерпретатором Python.',
                'presentations': [
                    {
                        'title': 'Знакомство с консолью',
                        'filename': 'Презентация_Python._Знакомство_с_консолью_134.pdf',
                    },
                ],
                'info': '<p>Консоль Python (интерпретатор) позволяет выполнять команды в интерактивном режиме.</p>',
            },
            {
                'id': 2,
                'title': 'Условные конструкции. Операции сравнения',
                'description': 'Работайте с if, else, elif и операторами сравнения.',
                'presentations': [
                    {
                        'title': 'Условные конструкции',
                        'filename': 'PY-88_Условные_конструкции._Операции_сравнения.pdf',
                    },
                ],
                'info': '<p>Условные конструкции позволяют программе выбирать разные пути выполнения.</p>',
            },
            {
                'id': 3,
                'title': 'Введение в типы данных',
                'description': 'Познакомьтесь с основными типами данных Python.',
                'presentations': [
                    {
                        'title': 'Типы данных',
                        'filename': 'Презентация_Введение_в_типы_данных_Анвартдинов_142.pdf',
                    },
                ],
                'info': '<p>Основные типы данных Python: int, float, str, bool, list, dict, tuple, set.</p>',
            },
            {
                'id': 4,
                'title': 'Циклы',
                'description': 'Повторяющиеся операции с циклами for и while.',
                'presentations': [
                    {
                        'title': 'Циклы',
                        'filename': 'Презентация_Циклы_Булыгин_142.pdf',
                    },
                ],
                'info': '<p>Циклы позволяют выполнять одну и ту же последовательность команд несколько раз.</p>',
            },
            {
                'id': 5,
                'title': 'Коллекции данных. Множества',
                'description': 'Изучите множества (set) — уникальные неупорядоченные коллекции.',
                'presentations': [
                    {
                        'title': 'Множества',
                        'filename': 'PY-122_Коллекции_данных._Множества.pdf',
                    },
                ],
                'info': '<p>Множества хранят уникальные элементы и полезны для проверки наличия без повторов.</p>',
            },
            {
                'id': 6,
                'title': 'Коллекции данных: словари',
                'description': 'Работа со словарями (dict) — структурами ключ-значение.',
                'presentations': [
                    {
                        'title': 'Словари',
                        'filename': 'py-144_Коллекции_данных__словари_Анвартдинов_edited.pdf',
                    },
                ],
                'info': '<p>Словари удобны для хранения данных по ключам и быстрых обращений.</p>',
            },
            {
                'id': 7,
                'title': 'Функции',
                'description': 'Использование встроенных и создание собственных функций.',
                'presentations': [
                    {
                        'title': 'Функции',
                        'filename': 'Презентация_Функции_PY_Булыгин_142.pdf',
                    },
                ],
                'info': '<p>Функции позволяют разбивать программу на логические блоки и переиспользовать код.</p>',
            },
        ],
    },
    {
        'id': 2,
        'title': 'SQL и базы данных',
        'description': 'Основы SQL и работы с базами данных (пока в разработке).',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Этот модуль будет содержать материал по базам данных.',
                'presentations': [],
                'info': '<p>Скоро здесь появится подробный контент по SQL и работе с базами данных.</p>',
            },
        ],
    },
    {
        'id': 3,
        'title': 'Web-разработка на Python',
        'description': 'Основы веб-разработки и протокола HTTP (пока в разработке).',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Этот модуль будет содержать материал по веб-разработке.',
                'presentations': [],
                'info': '<p>Скоро здесь появится подробный контент по основам веб-разработки и HTTP.</p>',
            },
        ],
    },
    {
        'id': 4,
        'title': 'JavaScript и Frontend',
        'description': 'Введение в JavaScript и фронтенд-разработку (пока в разработке).',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Этот модуль будет содержать материал по JavaScript.',
                'presentations': [],
                'info': '<p>Скоро здесь появится подробный контент по JavaScript и фронтенду.</p>',
            },
        ],
    },
    {
        'id': 5,
        'title': 'Тестирование и DevOps',
        'description': 'Основы тестирования и развертывания приложений (пока в разработке).',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Этот модуль будет содержать материал по тестированию и DevOps.',
                'presentations': [],
                'info': '<p>Скоро здесь появится подробный контент по тестированию и развертыванию.</p>',
            },
        ],
    },
    {
        'id': 6,
        'title': 'Django: создание backend-приложений',
        'description': 'Полный курс по Django для создания надежных веб-приложений и API.',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'header_image': settings.STATIC_URL + 'main/images/джанго заставка.webp',
        'info': '<p><strong>Django</strong> — это мощный фреймворк для создания веб-приложений на Python. Он предоставляет готовую функциональность для разработки полнофункциональных веб-сервисов, от небольших сайтов до высоконагруженных систем.</p><p>В этом модуле вы изучите все аспекты Django: от создания первого проекта до развертывания на боевом сервере. Материал основан на официальной документации и практических примерах с сайта Metanit.</p>',
        'topics': [
            {
                'id': 1,
                'title': 'Что такое Django',
                'description': 'Введение в фреймворк Django и архитектуру MVT.',
                'presentations': [],
                'info': '''
<h3>Что такое Django</h3>
<p>Django — это фреймворк для создания веб-приложений с помощью языка программирования Python. Он был создан в 2005 году веб-разработчиками газеты Lawrence Journal-World и с тех пор стал одним из самых популярных фреймворков в веб-разработке.</p>

<h3>История и популярность</h3>
<p>Django используется на многих известных сайтах, включая:</p>
<ul>
<li>Pinterest</li>
<li>Instagram</li>
<li>PBS</li>
<li>BitBucket</li>
<li>Washington Times</li>
<li>Mozilla</li>
</ul>

<h3>Преимущества Django</h3>
<ul>
<li><strong>Готовая функциональность:</strong> система аутентификации, генерация карт сайта, админ-панель и многое другое</li>
<li><strong>Безопасность:</strong> встроенная защита от SQL-инъекций, XSS-атак и CSRF-защита</li>
<li><strong>Масштабируемость:</strong> возможность создания приложений от небольших сайтов до высоконагруженных сервисов</li>
<li><strong>ORM (Object-Relational Mapping):</strong> удобная работа с базами данных без SQL</li>
<li><strong>Open Source:</strong> фреймворк бесплатен и развивается сообществом</li>
</ul>

<h3>Архитектура MVT (Model-View-Template)</h3>
<p>Django реализует архитектурный паттерн <strong>MVT</strong>, который является модификацией известного паттерна MVC (Model-View-Controller):</p>

<p><strong>Model (Модель):</strong> описывает данные приложения. Классы моделей соответствуют таблицам в базе данных.</p>
<p><strong>View (Представление):</strong> получает запрос, обрабатывает его и возвращает ответ. Может взаимодействовать с моделями и базой данных.</p>
<p><strong>Template (Шаблон):</strong> представляет логику создания HTML. Шаблоны содержат разметку с подставляемыми переменными из контекста.</p>
<p><strong>URL Dispatcher:</strong> маршрутизирует входящие запросы к нужным обработчикам на основе URL.</p>

<h3>Как работает запрос в Django</h3>
<ol>
<li>Пользователь отправляет запрос на URL сайта</li>
<li>URL Dispatcher анализирует URL и определяет, какой View должен обработать запрос</li>
<li>View получает запрос, обрабатывает его (может обращаться к Model и БД)</li>
<li>View генерирует ответ, часто используя Template для создания HTML</li>
<li>Ответ отправляется обратно браузеру пользователя</li>
</ol>

<h3>Версии Django</h3>
<p>На момент написания этого курса текущей версией является <strong>Django 6.0</strong>, которая вышла в декабре 2025 года. Регулярно выходят обновления и патчи безопасности.</p>
''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/django.png',
                        'caption': 'Django — мощный фреймворк для веб-приложений на Python.',
                    },
                ],
            },
            {
                'id': 2,
                'title': 'Установка и настройка Django',
                'description': 'Установка Django, создание виртуального окружения и проверка версии.',
                'presentations': [],
                'info': '''
<h3>Требования</h3>
<p>Прежде чем начать, убедитесь, что у вас установлен <strong>Python 3.11 или выше</strong>. Проверить версию можно командой:</p>
<pre>python --version</pre>

<h3>Пакетный менеджер pip</h3>
<p>Django распространяется через PyPI (Python Package Index). Для установки используется менеджер пакетов <strong>pip</strong>. Проверить версию pip:</p>
<pre>pip --version</pre>

<p>Обновить pip:</p>
<pre>python -m pip install --upgrade pip</pre>

<h3>Виртуальное окружение (venv)</h3>
<p>Рекомендуется использовать виртуальное окружение, чтобы изолировать зависимости проекта. Создание виртуального окружения:</p>
<pre>python -m venv .venv</pre>

<h3>Активация виртуального окружения</h3>
<p><strong>В Windows (Command Prompt):</strong></p>
<pre>.venv\\Scripts\\activate.bat</pre>

<p><strong>В Windows (PowerShell):</strong></p>
<pre>.venv\\Scripts\\Activate.ps1</pre>

<p><strong>В Linux/MacOS:</strong></p>
<pre>source .venv/bin/activate</pre>

<h3>Установка Django</h3>
<p>После активации виртуального окружения установите Django:</p>
<pre>pip install django</pre>

<p>Для установки конкретной версии:</p>
<pre>pip install django~=6.0.0</pre>

<h3>Проверка установки</h3>
<p>Проверьте, что Django установлен корректно:</p>
<pre>python -c "import django; print(django.get_version())"</pre>

<h3>Деактивация виртуального окружения</h3>
<p>Когда закончите работу:</p>
<pre>deactivate</pre>
''',
            },
            {
                'id': 3,
                'title': 'Создание первого проекта Django',
                'description': 'Инициализация проекта и понимание структуры папок.',
                'presentations': [],
                'info': '''
<h3>Команда startproject</h3>
<p>Для создания нового проекта Django используется утилита <strong>django-admin</strong> с командой <strong>startproject</strong>:</p>
<pre>django-admin startproject имя_проекта</pre>

<h3>Структура проекта</h3>
<p>После создания проекта вы получите следующую структуру:</p>
<pre>
имя_проекта/
    manage.py
    имя_проекта/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
</pre>

<h3>Назначение файлов</h3>

<p><strong>manage.py</strong> — главный скрипт проекта. С его помощью выполняются команды Django:
<ul>
<li><code>python manage.py runserver</code> — запуск сервера разработки</li>
<li><code>python manage.py startapp</code> — создание приложения</li>
<li><code>python manage.py migrate</code> — применение миграций</li>
<li><code>python manage.py collectstatic</code> — сбор статических файлов</li>
</ul>
</p>

<p><strong>settings.py</strong> — файл конфигурации проекта:
<ul>
<li>INSTALLED_APPS — список установленных приложений</li>
<li>MIDDLEWARE — список middleware</li>
<li>DATABASES — конфигурация базы данных</li>
<li>STATIC_URL, MEDIA_URL — пути к статике</li>
<li>SECRET_KEY — секретный ключ проекта</li>
<li>DEBUG — режим отладки</li>
</ul>
</p>

<p><strong>urls.py</strong> — главный файл маршрутизации. Здесь определяются URL-адреса проекта и связываются с представлениями.</p>

<p><strong>wsgi.py</strong> — конфигурация WSGI (Web Server Gateway Interface) для развертывания на боевом сервере.</p>

<p><strong>asgi.py</strong> — конфигурация ASGI (Asynchronous Server Gateway Interface) для асинхронных приложений.</p>

<h3>Запуск проекта</h3>
<p>Перейдите в папку проекта и запустите сервер разработки:</p>
<pre>cd имя_проекта
python manage.py runserver</pre>

<p>Сервер запустится по адресу <strong>http://127.0.0.1:8000/</strong>. Откройте этот адрес в браузере и увидите приветственную страницу Django.</p>

<h3>Остановка сервера</h3>
<p>Нажмите <strong>Ctrl+C</strong> в терминале для остановки сервера.</p>
''',
            },
            {
                'id': 4,
                'title': 'Создание первого приложения',
                'description': 'Структура приложения, views.py, models.py и другие файлы.',
                'presentations': [],
                'info': '''
<h3>Что такое приложение в Django</h3>
<p>Проект Django состоит из <strong>приложений</strong>. Каждое приложение — это модуль с определенной функциональностью:</p>
<ul>
<li>Приложение может содержать модели, представления, шаблоны</li>
<li>Приложения можно переносить между проектами</li>
<li>Один проект может содержать множество приложений</li>
</ul>

<h3>Встроенные приложения</h3>
<p>При создании проекта в <strong>settings.py</strong> уже есть приложения по умолчанию:</p>
<pre>
INSTALLED_APPS = [
    'django.contrib.admin',      # администратор
    'django.contrib.auth',       # аутентификация
    'django.contrib.contenttypes', # типы контента
    'django.contrib.sessions',   # сессии
    'django.contrib.messages',   # сообщения
    'django.contrib.staticfiles', # статические файлы
]
</pre>

<h3>Создание приложения</h3>
<p>Используется команда <strong>startapp</strong>:</p>
<pre>python manage.py startapp имя_приложения</pre>

<p>Например, создадим приложение <strong>hello</strong>:</p>
<pre>python manage.py startapp hello</pre>

<h3>Структура приложения</h3>
<p>После создания приложение содержит:</p>
<pre>
hello/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
</pre>

<h3>Назначение файлов приложения</h3>

<p><strong>migrations/</strong> — папка для хранения миграций (скрипты синхронизации БД).</p>

<p><strong>__init__.py</strong> — указывает Python, что это пакет.</p>

<p><strong>admin.py</strong> — регистрация моделей в админ-панели Django.</p>

<p><strong>apps.py</strong> — конфигурация приложения (имя, метка и т.д.).</p>

<p><strong>models.py</strong> — определение моделей данных (таблиц БД).</p>

<p><strong>tests.py</strong> — модульные тесты приложения.</p>

<p><strong>views.py</strong> — функции представлений, которые обрабатывают запросы.</p>

<h3>Регистрация приложения</h3>
<p>Чтобы приложение работало, добавьте его в <strong>settings.py</strong>:</p>
<pre>
INSTALLED_APPS = [
    ...
    'hello',  # добавляем наше приложение
]
</pre>

<h3>Первое представление</h3>
<p>В файле <strong>views.py</strong> создайте простое представление:</p>
<pre>
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello METANIT.COM")
</pre>

<p>Затем в <strong>urls.py</strong> проекта добавьте маршрут:</p>
<pre>
from django.urls import path
from hello import views

urlpatterns = [
    path('', views.index, name='home'),
]
</pre>

<p>Теперь при открытии <strong>http://127.0.0.1:8000/</strong> вы увидите "Hello METANIT.COM".</p>
''',
            },
        ],
    },
]


def test_page(request):
    return HttpResponse("This is a test page.")


def module_list(request):
    return render(request, 'module_list.html', {'modules': MODULES, 'banner': settings.MEDIA_URL + 'banner.png'})


def module_detail(request, module_id):
    module = next((module for module in MODULES if module['id'] == module_id), None)
    if not module:
        raise Http404('Модуль не найден')
    return render(request, 'module_detail.html', {'module': module})


def topic_detail(request, module_id, topic_id):
    module = next((module for module in MODULES if module['id'] == module_id), None)
    if not module:
        raise Http404('Модуль не найден')
    
    topic = next((topic for topic in module['topics'] if topic['id'] == topic_id), None)
    if not topic:
        raise Http404('Тема не найдена')
    
    presentations = []
    for pres in topic['presentations']:
        presentations.append({
            'title': pres['title'],
            'filename': pres['filename'],
        })
    
    return render(request, 'topic_detail.html', {'module': module, 'topic': topic, 'presentations': presentations})


def product(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, template_name='details.html', context={'product': product})

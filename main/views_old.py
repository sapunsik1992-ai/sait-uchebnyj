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
        'title': 'Django',
        'description': 'Основной модуль по веб-разработке на Django с метанит-информацией и презентацией.',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'header_image': settings.STATIC_URL + 'main/images/джанго заставка.webp',
        'info': '<p>Этот модуль содержит подробное введение в Django, примеры кода и карточки, как в Word-документе.</p><p>Здесь вы найдете объяснение структуры проекта, приложений, маршрутов, шаблонов и статических файлов.</p>',
        'topics': [
            {
                'id': 1,
                'title': 'Введение в Django',
                'description': 'Содержит пояснения, примеры и картинки по основам Django из Metanit.',
                'presentations': [],
                'info': '''
                    <h3>Что такое Django</h3>
                    <p>Django — это фреймворк на Python для создания веб-приложений. Он дает готовую структуру проекта, маршруты, шаблоны, работу с формами и моделями.</p>
                    <p>Этот модуль основан на материалах сайта Metanit и расширяет их подробными пояснениями.</p>
                    <h3>Установка и запуск</h3>
                    <p>Первый шаг — установить Django в виртуальное окружение. Создайте папку проекта, активируйте venv и выполните:</p>
                    <pre>python -m pip install django</pre>
                    <p>После этого создайте проект:</p>
                    <pre>django-admin startproject my_project .</pre>
                    <h3>Структура Django-проекта</h3>
                    <p>В папке `my_project` находятся настройки, URLs и серверный файл WSGI. В корне проекта есть `manage.py` для запуска сервера и управления миграциями.</p>
                    <h3>Приложения</h3>
                    <p>Каждое приложение Django хранит свою логику: модели, представления, шаблоны и статические файлы. В нашем сайте приложение называется `main`.</p>
                    <h3>Маршрутизация</h3>
                    <p>URL-адреса определяются в `urls.py`. В проекте мы подключаем маршруты модуля `main` и оставляем путь к административной панели.</p>
                    <h3>Шаблоны</h3>
                    <p>Шаблоны HTML хранятся в `main/templates/` и используют синтаксис Django для передачи данных. Мы используем функции `render` в `views.py`.</p>
                    <h3>Статические файлы</h3>
                    <p>CSS, изображения и документы хранятся в `main/static/main/`. В шаблонах они подключаются через тег `{% load static %}`.</p>
                    <h3>Дальнейшие темы</h3>
                    <p>После введения идут темы: представления, шаблоны, формы, модели и работа с базой данных. В этом модуле мы начнем именно с базовой структуры, чтобы вам было проще переходить к следующим главам.</p>
                ''',
                'images': [
                    {
                        'src': settings.STATIC_URL + 'main/images/django.png',
                        'caption': 'Django — фреймворк для веб-приложений на Python.',
                    },
                    {
                        'src': settings.STATIC_URL + 'main/images/джанго заставка.webp',
                        'caption': 'Схема проекта Django: приложение, шаблоны, маршруты.',
                    },
                ],
            },
            {
                'id': 2,
                'title': 'Презентация по Django',
                'description': 'Откройте презентацию и изучите введение в Django.',
                'presentations': [
                    {
                        'title': 'Знакомство с Django: подготовка и запуск проекта',
                        'filename': '4.1._Знакомство_с_Django._Подготовка_и_запуск_проекта_1404.pdf',
                    },
                    {
                        'title': 'DJ 1.1. Знакомство с Django. Подготовка и запуск проекта',
                        'filename': 'DJ_1.1._Знакомство_с_Django._Подготовка_и_запуск_проекта__1_.pdf',
                    },
                ],
                'info': '<p>Эта презентация поможет вам увидеть основные шаги создания проекта Django: установка, конфигурация и первый запуск.</p>',
            },
        ],
    },
    {
        'id': 3,
        'title': 'Django. Представления и маршруты',
        'description': 'Пока содержимое в разработке, позже добавим темы по URL, HttpRequest и HttpResponse.',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Страница пока пустая — в будущем тут появятся темы по маршрутам и представлениям.',
                'presentations': [],
                'info': '<p>Этот модуль будет посвящен обработке запросов, маршрутам и возвращаемым ответам в Django.</p>',
            },
        ],
    },
    {
        'id': 4,
        'title': 'Django. Шаблоны',
        'description': 'Пока пусто. В будущем добавить шаблоны, статические файлы и работу с формами.',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Страница пока пустая — здесь появятся темы по шаблонам Django.',
                'presentations': [],
                'info': '<p>Шаблоны Django позволяют разделять структуру страницы и данные, передаваемые из представлений.</p>',
            },
        ],
    },
    {
        'id': 5,
        'title': 'Django. Формы',
        'description': 'Содержимое будет добавлено позже: работа с формами и валидация.',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Здесь будет материал по формам Django и обработке POST-запросов.',
                'presentations': [],
                'info': '<p>Формы Django помогают собирать данные от пользователей и проверять их правильность.</p>',
            },
        ],
    },
    {
        'id': 6,
        'title': 'Django. Модели',
        'description': 'Пока пусто — будет материал по моделям, миграциям и работе с базой данных.',
        'icon': settings.MEDIA_URL + 'module-icon.webp',
        'topics': [
            {
                'id': 1,
                'title': 'Содержимое в разработке',
                'description': 'Страница пока пустая — здесь добавим темы по моделям и ORM.',
                'presentations': [],
                'info': '<p>Модели в Django описывают структуру данных и помогают сохранять информацию в базе.</p>',
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

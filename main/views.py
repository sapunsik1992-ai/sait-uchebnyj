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
                'description': 'Вторая тема. Работайте с if, else, elif и операторами сравнения.',
                'presentations': [
                    {
                        'title': 'Условные конструкции',
                        'filename': 'PY-88_Условные_конструкции._Операции_сравнения.pdf',
                    },
                ],
                'info': '<p>Условные конструкции позволяют программе выбирать различные пути выполнения.</p>',
            },
            {
                'id': 3,
                'title': 'Введение в типы данных',
                'description': 'Третья тема. Познакомьтесь с основными типами данных в Python.',
                'presentations': [
                    {
                        'title': 'Типы данных',
                        'filename': 'Презентация_Введение_в_типы_данных_Анвартдинов_142.pdf',
                    },
                ],
                'info': '<p>Основные типы данных: int, float, str, bool, list, dict, tuple, set.</p>',
            },
            {
                'id': 4,
                'title': 'Циклы',
                'description': 'Четвёртая тема. Повторяющиеся операции с циклами for и while.',
                'presentations': [
                    {
                        'title': 'Циклы',
                        'filename': 'Презентация_Циклы_Булыгин_142.pdf',
                    },
                ],
                'info': '<p>Циклы позволяют повторять один и тот же код несколько раз.</p>',
            },
            {
                'id': 5,
                'title': 'Коллекции данных. Множества',
                'description': 'Пятая тема. Изучите множества (set) — неупорядоченные коллекции.',
                'presentations': [
                    {
                        'title': 'Множества',
                        'filename': 'PY-122_Коллекции_данных._Множества.pdf',
                    },
                ],
                'info': '<p>Множества — это неупорядоченные коллекции уникальных элементов.</p>',
            },
            {
                'id': 6,
                'title': 'Коллекции данных: словари',
                'description': 'Шестая тема. Работайте со словарями (dict) — структурами ключ-значение.',
                'presentations': [
                    {
                        'title': 'Словари',
                        'filename': 'py-144_Коллекции_данных__словари_Анвартдинов_edited.pdf',
                    },
                ],
                'info': '<p>Словари — это упорядоченные коллекции пар ключ-значение.</p>',
            },
            {
                'id': 7,
                'title': 'Функции - использование встроенных и создание собственных',
                'description': 'Седьмая тема. Функции для повторного использования кода.',
                'presentations': [
                    {
                        'title': 'Функции',
                        'filename': 'Презентация_Функции_PY_Булыгин_142.pdf',
                    },
                ],
                'info': '<p>Функции позволяют группировать код и повторно использовать его.</p>',
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
    
    # Добавляем URL к презентациям
    presentations = []
    for pres in topic['presentations']:
        presentations.append({
            'title': pres['title'],
            'url': settings.MEDIA_URL + 'presentations/module1/' + pres['filename'],
        })
    
    return render(request, 'topic_detail.html', {'module': module, 'topic': topic, 'presentations': presentations})


def product(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, template_name='details.html', context={'product': product})

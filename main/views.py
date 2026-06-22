import json
import logging
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from main.models import AssistantMessage, Module, Topic, Product

logger = logging.getLogger(__name__)


def test_page(request):
    return HttpResponse("This is a test page.")


def get_common_context():
    return {
        'admin_url': '/admin/',
        'assistant_url': '/assistant/',
        'assistant_enabled': bool(os.environ.get('HUGGINGFACE_API_KEY')),
    }


def module_list(request):
    modules = Module.objects.all().order_by('order')
    context = get_common_context()
    context.update({
        'modules': modules,
        'banner': settings.MEDIA_URL + 'banner.png',
    })
    return render(request, 'module_list.html', context)


def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    topics = module.topics.all()
    context = get_common_context()
    context.update({
        'module': module,
        'topics': topics,
    })
    return render(request, 'module_detail.html', context)


def topic_detail(request, module_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, module_id=module_id)
    presentations = topic.presentations.filter(file__isnull=False)
    images = topic.images.filter(image__isnull=False)
    context = get_common_context()
    context.update({
        'module': topic.module,
        'topic': topic,
        'presentations': presentations,
        'images': images,
    })
    return render(request, 'topic_detail.html', context)


def assistant_help(request):
    recent_messages = AssistantMessage.objects.all()[:10]
    context = get_common_context()
    context.update({
        'recent_messages': recent_messages,
    })
    return render(request, 'assistant.html', context)


def assistant_history(request):
    messages = AssistantMessage.objects.all()[:20]
    data = [{'role': m.role, 'text': m.text, 'created_at': m.created_at.isoformat()} for m in messages]
    return JsonResponse({'messages': data})


@require_POST
def assistant_api(request):
    question = request.POST.get('question', '').strip()
    if question:
        AssistantMessage.objects.create(role='user', text=question)
    answer = get_assistant_answer(question)
    AssistantMessage.objects.create(role='assistant', text=answer)
    return JsonResponse({'answer': answer})


def get_assistant_answer(question):
    text = question.strip()
    api_key = os.environ.get('HUGGINGFACE_API_KEY')
    if api_key and text:
        try:
            return call_huggingface_assistant(text, api_key)
        except Exception:
            return get_local_assistant_answer(text, external_disabled=False)
    return get_local_assistant_answer(text, external_disabled=not bool(api_key))


def call_huggingface_assistant(question, api_key):
    """Вызывает HuggingFace API для получения ответа"""
    url = 'https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    
    data = {
        'model': 'mistralai/Mistral-7B-Instruct-v0.3',
        'messages': [
            {
                'role': 'system',
                'content': '''Ты - полезный AI-помощник для учебного портала на Django.

Твоя задача:
1. Помогать пользователю с редактированием сайта через админку Django
2. Помогать в обучении Python - объяснять код, концепции, ошибки
3. Давать советы по структуре модулей и тем

Всегда отвечай на русском языке. Будь кратким, но полезным. Если нужно показать код - используй форматирование.'''
            },
            {'role': 'user', 'content': question},
        ],
        'temperature': 0.7,
        'max_tokens': 1024,
    }
    request_obj = Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        response = urlopen(request_obj, timeout=30)
        response_data = json.loads(response.read().decode('utf-8'))
        return response_data['choices'][0]['message']['content'].strip()
    except HTTPError as exc:
        try:
            body = exc.read().decode('utf-8')
        except Exception:
            body = '<no response body>'
        logger.error('HuggingFace HTTPError %s: %s', exc.code, body)
        return 'Не удалось подключиться к AI-помощнику. Использую локальный режим.'
    except URLError as exc:
        logger.error('HuggingFace URLError: %s', exc)
        return f'Нет подключения к HuggingFace API. Ошибка: {exc}. Проверьте интернет-соединение.'
    except Exception as exc:
        logger.exception('HuggingFace request failed')
        return 'Ошибка AI-помощника. Использую локальный режим.'


def get_local_assistant_answer(question, external_disabled=True):
    text = question.lower()
    if not text:
        if external_disabled:
            return ('Напишите ваш вопрос, и я постараюсь помочь. Эта версия работает локально. ' 
                    'Для умного AI-помощника добавьте переменную окружения HUGGINGFACE_API_KEY.')
        return 'Напишите ваш вопрос, и я постараюсь помочь с админкой или учебным содержанием.'
    
    # Правила для админки
    if 'модул' in text or 'тема' in text or 'курс' in text:
        return ('Чтобы открыть модуль, нажмите на карточку модуля на главной странице. '
                'Внутри модуля выберите тему, чтобы увидеть содержимое, презентации и иллюстрации.')
    
    if 'админ' in text or 'admin' in text or 'панел' in text:
        return ('Админка доступна по адресу /admin/. Она нужна только для редактирования. '
                'Основной сайт открыт всем, а админка — только вам.')
    
    if 'создать пользователя' in text or 'супер' in text or 'superuser' in text:
        return ('Суперпользователь создаётся автоматически при первом запуске. '
                'Вход по логину admin и паролю Admin1234, если вы не меняли учётные данные.')
    
    if 'добавить тему' in text or 'новая тема' in text:
        return ('В админке откройте нужный модуль и в конце списка тем нажмите "Добавить ещё одну тему". '
                'Заполните название, описание и текст урока, затем сохраните.')
    
    if 'презентац' in text or 'файл' in text or 'ppt' in text:
        return ('В теме можно прикрепить презентацию через раздел "Presentations". '
                'Нажмите "Добавить" и загрузите файл в формате PDF или PPTX.')
    
    if 'изображ' in text or 'картин' in text:
        return ('Иллюстрации добавляются через раздел "Topic images" в админке темы. '
                'Загрузите картинку и укажите подпись, чтобы она отображалась в уроке.')
    
    if 'учеб' in text or 'как учить' in text or 'практик' in text:
        return ('Читать материал и сразу повторять примеры — лучший способ. '
                'Пробуйте запускать команды, писать небольшой код и проверять результат прямо на сайте.')
    
    if 'python' in text or 'код' in text or 'функци' in text or 'переменн' in text:
        return ('Я могу помочь с Python! Задайте вопрос про код, функции, списки, словари или любую другую тему. '
                'Например: "как сделать цикл", "что такое list comprehension", "как обработать ошибку"')
    
    if 'django' in text or 'модель' in text or 'миграц' in text:
        return ('Я помогу с Django! Спросите про модели, админку, миграции или любую другую тему фреймворка.')
    
    if external_disabled:
        return ('Я пока локальный помощник сайта и могу давать общие советы. '
                'Для более умного ответа нужно установить HUGGINGFACE_API_KEY в настройках Render.')
    
    return ('Я работаю на HuggingFace AI (Mistral-7B). Задайте вопрос про сайт, админку, Python или Django, и я постараюсь ответить как эксперт.')


def product(request):
    products = Product.objects.all()
    context = get_common_context()
    context.update({'products': products})
    return render(request, 'products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = get_common_context()
    context.update({'product': product})
    return render(request, template_name='details.html', context=context)

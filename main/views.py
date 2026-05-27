import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from main.models import AssistantMessage, Module, Topic, Product


def test_page(request):
    return HttpResponse("This is a test page.")


def module_list(request):
    modules = Module.objects.all().order_by('order')
    return render(request, 'module_list.html', {
        'modules': modules,
        'banner': settings.MEDIA_URL + 'banner.png',
        'admin_url': '/admin/',
        'assistant_url': '/assistant/',
    })


def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    topics = module.topics.all()
    return render(request, 'module_detail.html', {
        'module': module,
        'topics': topics,
        'admin_url': '/admin/',
        'assistant_url': '/assistant/',
    })


def topic_detail(request, module_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, module_id=module_id)
    presentations = topic.presentations.filter(file__isnull=False)
    images = topic.images.filter(image__isnull=False)
    return render(request, 'topic_detail.html', {
        'module': topic.module,
        'topic': topic,
        'presentations': presentations,
        'images': images,
        'admin_url': '/admin/',
        'assistant_url': '/assistant/',
    })


def assistant_help(request):
    recent_messages = AssistantMessage.objects.all()[:10]
    return render(request, 'assistant.html', {
        'recent_messages': recent_messages,
        'admin_url': '/admin/',
    })


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
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        try:
            return call_openai_assistant(question, api_key)
        except Exception:
            pass
    return get_local_assistant_answer(question)


def call_openai_assistant(question, api_key):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'Ты помогаешь пользователю с сайтом учебного портала и админкой Django.'},
            {'role': 'user', 'content': question},
        ],
        'temperature': 0.7,
        'max_tokens': 400,
    }
    request = Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        response = urlopen(request, timeout=15)
        response_data = json.loads(response.read().decode('utf-8'))
        return response_data['choices'][0]['message']['content'].strip()
    except HTTPError as exc:
        return 'Не удалось подключиться к внешнему помощнику. Использую локальный режим.'
    except URLError as exc:
        return 'Сеть недоступна. Использую локальный помощник.'
    except Exception:
        return 'Ошибка внешнего AI. Использую локальный помощник.'


def get_local_assistant_answer(question):
    text = question.lower()
    if not text:
        return 'Напишите ваш вопрос, и я постараюсь помочь с админкой или учебным содержанием.'
    if 'модул' in text or 'тема' in text or 'курс' in text:
        return ('Чтобы открыть модуль, нажмите на карточку модуля на главной странице. ' 
                'Внутри модуля выберите тему, чтобы увидеть содержимое, презентации и иллюстрации.')
    if 'админ' in text or 'admin' in text or 'панел' in text:
        return ('Админка позволяет создавать и изменять модульные темы, презентации и картинки. ' 
                'Сначала создайте модуль, затем добавьте к нему темы, а в теме укажите информацию и медиа.')
    if 'создать пользователя' in text or 'супер' in text or 'superuser' in text:
        return ('Суперпользователь уже создан. Для входа используйте логин admin и пароль Admin1234. ' 
                'Если хотите, можно сменить пароль в админке через "Изменить пароль".')
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
    return ('Я пока локальный помощник сайта. Задайте вопрос про модули, админку или учебные темы, например: "Как добавить модуль?".')


def product(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, template_name='details.html', context={'product': product})

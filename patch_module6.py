from pathlib import Path

path = Path('main/views.py')
text = path.read_text(encoding='utf-8')
start = text.index("        'id': 6,\n        'title': 'Django: создание backend-приложений'")
start = text.rfind("    {", 0, start)
end = text.index("        ],\n    },\n]", start) + len("        ],\n    },\n]")
new_block = r"""    {
                'id': 6,
                'title': 'Глава 6. Создание сайта Django',
                'description': 'Пошаговый учебный отчет по созданию реального сайта Django.',
                'presentations': [
                    {
                        'title': 'Пошаговый учебный отчет по созданию сайта Django',
                        'filename': 'Django_Пошаговый_Отчет.pdf',
                    },
                ],
                'info': r'''
<h3>1. Подготовка рабочего места</h3>
<p>Создайте рабочую папку и перейдите в неё:</p>
<pre>mkdir "C:\Users\titi\Desktop\ДЖАНГО"
cd "C:\Users\titi\Desktop\ДЖАНГО"</pre>

<h3>2. Виртуальное окружение</h3>
<p>Создайте и активируйте виртуальное окружение:</p>
<pre>python -m venv .venv
.\.venv\Scripts\Activate.ps1</pre>
<p>Установите зависимости:</p>
<pre>python -m pip install --upgrade pip
python -m pip install django python-docx reportlab</pre>

<h3>3. Создание проекта и приложения</h3>
<p>Инициализируйте проект и создайте приложение:</p>
<pre>django-admin startproject my_project .
python manage.py startapp main</pre>

<h3>4. Регистрация приложения и маршрутов</h3>
<p>Добавьте приложение <code>main</code> в <code>INSTALLED_APPS</code> и пропишите URL-маршруты в <code>my_project/urls.py</code>.</p>

<h3>5. Реализация логики</h3>
<p>В <code>main/views.py</code> оформите список модулей и тем. Команды должны возвращать HTML-страницы с данными.</p>

<h3>6. Работа с базой и админкой</h3>
<p>Создайте модели, выполните миграции и зарегистрируйте их в <code>admin.py</code>, чтобы удобно управлять данными.</p>

<h3>7. Сбор статики и деплой</h3>
<p>Для продакшена выполните:</p>
<pre>python manage.py collectstatic --noinput</pre>
<p>Используйте <code>whitenoise</code> и настройки <code>STATIC_ROOT</code>, <code>STATIC_URL</code>, <code>MEDIA_ROOT</code>, <code>MEDIA_URL</code>.</p>

<h3>8. Проверка локально</h3>
<p>Запустите сервер и проверьте доступность страниц:</p>
<pre>python manage.py runserver</pre>

<h3>9. Учебный отчёт</h3>
<p>В приложенном PDF находятся подробные шаги и примеры команд для повторения проекта.</p>
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
text = text[:start] + new_block + text[end:]
path.write_text(text, encoding='utf-8')
print('module 6 restored')

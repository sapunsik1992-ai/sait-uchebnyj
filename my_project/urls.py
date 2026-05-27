from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import assistant_api, assistant_history, assistant_help, module_list, module_detail, product, product_detail, test_page, topic_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/assistant/', admin.site.admin_view(assistant_help), name='admin_assistant'),
    path('assistant/', assistant_help, name='assistant_help'),
    path('assistant/api/', assistant_api, name='assistant_api'),
    path('assistant/history/', assistant_history, name='assistant_history'),
    path('', module_list, name='module_list'),
    path('index/', module_list),
    path('modules/<int:module_id>/', module_detail, name='module_detail'),
    path('modules/<int:module_id>/topics/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('products/', product, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

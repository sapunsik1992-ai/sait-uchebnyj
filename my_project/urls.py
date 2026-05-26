from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import module_list, module_detail, topic_detail, product, product_detail, test_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', module_list, name='module_list'),
    path('index/', module_list),
    path('modules/<int:module_id>/', module_detail, name='module_detail'),
    path('modules/<int:module_id>/topics/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('products/', product, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

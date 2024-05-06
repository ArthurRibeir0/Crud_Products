from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_API_Produtos.urls'), name='app_API_Produtos.urls'),
]

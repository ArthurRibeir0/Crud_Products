from django.urls import path
from . import views

# Lista de padrões de URL para o aplicativo
urlpatterns = [
    # Define uma rota para a lista de produtos
    path('products/', views.product_list, name='product-list'),

    # Define uma rota para detalhes de um produto específico
    path('products/<int:pk>/', views.product_detail, name='product-detail'),


    # path('', views.get_product, name='get_all_products'),
    # path('product/<int:pk>/', views.get_by_id, name='get_by_id'),
    # path('data/', views.product_manager),
]

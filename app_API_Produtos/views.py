from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer



# Função de lista de produtos para métodos GET e POST
@api_view(['GET', 'POST'])
def product_list(request):
    # Retorna todos os produtos no banco de dados se o método for GET
    # ou cria um novo produto se o método for POST
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Função de detalhes de produto para métodos GET, PUT e DELETE
@api_view(['GET', 'PATCH', 'DELETE'])
def product_detail(request, pk):
    try:
        # Tenta encontrar um produto com o ID fornecido na requisição
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # Se o produto não for encontrado, retorna 404
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Retorna os detalhes do produto se o método for GET
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    # Atualiza os detalhes do produto se o método for PUT
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Exclui o produto se o método for DELETE
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


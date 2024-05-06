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
@api_view(['GET', 'PUT', 'DELETE'])
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
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Exclui o produto se o método for DELETE
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# # Decorador para indicar que esta função é uma view de API RESTful que responde aos métodos GET e POST
# @api_view(['GET', 'POST'])
# def product_list(request):
#     # Verifica o método HTTP da requisição
#     if request.method == 'GET':
#         # Recupera todos os produtos do banco de dados
#         products = Product.objects.all()
#         # Serializa os produtos para transformá-los em JSON
#         serializer = ProductSerializer(products, many=True)
#         # Retorna uma resposta HTTP com os dados serializados
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # Serializa os dados recebidos na requisição em um objeto ProductSerializer
#         serializer = ProductSerializer(data=request.data)
#         # Verifica se os dados são válidos
#         if serializer.is_valid():
#             # Salva os dados no banco de dados
#             serializer.save()
#             # Retorna uma resposta HTTP com os dados serializados e o código de status 201 Created
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Caso os dados não sejam válidos, retorna uma resposta com os erros de validação e o código de status 400 Bad Request
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Decorador para indicar que esta função é uma view de API RESTful que responde aos métodos GET, PUT e DELETE
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     try:
#         # Tenta encontrar um produto com o ID fornecido na requisição
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         # Se o produto não for encontrado, retorna uma resposta com o código de status 404 Not Found
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # Se o método da requisição for GET, retorna os dados do produto encontrado
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     # Se o método da requisição for PUT, atualiza os dados do produto com os dados fornecidos na requisição
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # Se o método da requisição for DELETE, exclui o produto do banco de dados
#     elif request.method == 'DELETE':
#         product.delete()
#         # Retorna uma resposta sem conteúdo com o código de status 204 No Content
#         return Response(status=status.HTTP_204_NO_CONTENT)







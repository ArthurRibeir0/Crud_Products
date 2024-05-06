from rest_framework import serializers
from .models import Product

# Definição do serializer para a classe Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # Indica qual modelo será serializado por este serializer
        model = Product
        # Define quais campos do modelo serão incluídos na serialização.
        # Usar '__all__' significa que todos os campos do modelo serão incluídos
        fields = '__all__'

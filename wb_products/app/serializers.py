from rest_framework import serializers
from .models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()

    class Meta:
        model = Product
        fields = '__all__'

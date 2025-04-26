from rest_framework import serializers
from product.models import Product, ProductImage, ProductView
from api.category.serializers import CategorySerializer, RegionSerializer, BrandSerializer
from api.user.serializers import ProfilerSeralizer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = ProfilerSeralizer()
    location = RegionSerializer()
    brand = BrandSerializer
    class Meta:
        model = Product
        fields = ["id", "title", "location", "category", "brand", "user", "condition", "status", "price", "created_at"]
        
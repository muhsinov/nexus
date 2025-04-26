from rest_framework import serializers
from category.models import Category, Region, Brand

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'is_main']
        
class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ["id", "name", "sorting"]

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ["id", "name"]
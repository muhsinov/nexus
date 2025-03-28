from django.db.models import Prefetch
from django.shortcuts import render
from category.models import Category, Region
from product.models import Product, ProductImage


def main(request):
    return render(request, 'index.html')


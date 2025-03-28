from django.db.models import Prefetch
from django.shortcuts import render
from category.models import Category, Region
from product.models import Product, ProductImage


def main(request):
    products = Product.objects.prefetch_related(Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))[:3]
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    ctx = {
        "products": products,
        "categories": categories,
        "regions": regions
    }
    return render(request, 'index.html', ctx)


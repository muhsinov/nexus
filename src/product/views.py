from django.shortcuts import render
from django.db.models import Prefetch
from category.models import Category, Region
from product.models import Product, ProductImage
from django.core.paginator import Paginator


def product(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = Product.objects.prefetch_related(Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))

    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_products = paginator.get_page(page_number)

    ctx = {
        "categories": categories,
        "regions" : regions,
        "products" : products,
        "page_products" : page_products
    }
    return render(request, 'product.html', ctx)



def detail(request, pk):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    product = Product.objects.prefetch_related('images').get(pk=pk)

    ctx = {
        "categories": categories,
        "regions" : regions,
        "product" : product
    }

    return render(request, 'detail.html', ctx)
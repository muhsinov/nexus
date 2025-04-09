from django.shortcuts import render, redirect
from django.db.models import Prefetch
from category.models import Category, Region
from .models import Product, ProductImage
from django.core.paginator import Paginator
from .forms import ProductForm, ImageForm
from django.contrib.auth.decorators import login_required


def product(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = Product.objects.prefetch_related(Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))

    paginator = Paginator(products, 4)
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
        "product" : product,
        "pk": pk
    }

    return render(request, 'detail.html', ctx)


@login_required(login_url='login')
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        images = request.FILES.getlist('images')
        

        if form.is_valid() and images:
            product = form.save(commit=False)
            product.user = request.user.profile
            product.save()
            
            for image in images: 
                image_instance = ProductImage(product=product, image=image)
                image_instance.save()

            return redirect('product-detail', pk=product.pk)
        else:
            print("*" * 10)
            print(form.errors)
            print(images)

    else:
        form = ProductForm()
        images = ImageForm()
        
    ctx = {
        'form': form,
        'images': images,
    }

    return render(request, 'product-add.html', ctx)


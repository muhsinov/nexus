from django.urls import path
from .views import product, detail, product_add

urlpatterns = [
    path('', product, name='product'),
    path('include/<int:pk>', detail, name='product-detail'),
    path('add/', product_add, name='product-add'),
]

    
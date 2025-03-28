from django.urls import path
from .views import product, detail

urlpatterns = [
    path('', product, name='product'),
    path('include/<int:pk>', detail, name='product-detail')
]


from django.urls import path
from .views import get_products, get_product

urlpatterns = [
    path("", get_products, name='get-products'),
    path("detail/<int:pk>/", get_product, name="get-product")
]
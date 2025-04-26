from django.urls import path
from .views import get_category, ctg_detail

urlpatterns = [
    path('', get_category, name="categories"),
    path('detail/<int:pk>/', ctg_detail, name="category"),
]
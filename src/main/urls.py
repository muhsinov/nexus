from django.urls import path, include
from .views import main, contact

urlpatterns = [
    path('', main, name='main'),
    path('contact/', contact, name='contact')
]

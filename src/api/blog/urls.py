from django.urls import path
from .views import BlogGenericAPIView, BlogDetailGenericAPIView

urlpatterns = [
    path('', BlogGenericAPIView.as_view()),
    path('detail/<int:pk>/', BlogDetailGenericAPIView.as_view()),
    # path('detail/<int:pk>/', BlogDetailGenericAPIView.as_view()),
]
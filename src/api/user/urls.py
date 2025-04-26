from django.urls import path
from .views import get_user, get_users

urlpatterns = [
    path("", get_users, name="get-users"),
    path("detail/<int:pk>/", get_user, name="get-user")
]

# core/urls.py
from django.urls import path
from .views import  UserRoleView

urlpatterns = [
    path('user/role/', UserRoleView.as_view(), name='user_role'),  # Endpoint for checking user role
]

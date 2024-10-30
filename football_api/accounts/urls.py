from django.urls import path
from .views import RegisterView, GoogleLogin, FacebookLogin
from .views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),  # User registration
    path('google/', GoogleLogin.as_view(), name='google_login'),  # Google login
    path('facebook/', FacebookLogin.as_view(), name='facebook_login'),  # Facebook login
       path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

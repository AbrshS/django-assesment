from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from core.models import CustomUser  # Import your custom user model
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import PasswordResetSerializer, PasswordResetConfirmSerializer

# Register API
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Use CustomUser instead of User
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class GoogleLogin(SocialLoginView):  # Google social login view
    adapter_class = GoogleOAuth2Adapter

class FacebookLogin(SocialLoginView):  # Facebook social login view
    adapter_class = FacebookOAuth2Adapter


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data['email'])
        
        # Create password reset token and send email
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        
        reset_link = f"http://127.0.0.1:8000/accounts/password_reset_confirm/{uid}/{token}/"
        send_mail(
            'Password Reset Request',
            f'Please click the link to reset your password: {reset_link}',
            'from@example.com',  # Replace with your email
            [user.email],
            fail_silently=False,
        )
        
        return Response({"detail": "Password reset email has been sent."}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, uidb64, token):
        serializer = self.get_serializer(data={**request.data, 'uidb64': uidb64, 'token': token})
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(pk=urlsafe_base64_decode(uidb64).decode())
        user.set_password(serializer.validated_data['password'])
        user.save()
        
        return Response({"detail": "Password has been reset successfully."}, status=status.HTTP_200_OK)

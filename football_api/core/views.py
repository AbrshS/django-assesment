from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import CustomUser

class UserRoleView(APIView):
    """
    API endpoint to retrieve the role of the logged-in user.
    Only authenticated users can access this endpoint.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieve the role information of the authenticated user.
        """
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


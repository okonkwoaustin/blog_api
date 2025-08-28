from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from blogs.models import Blog
from .serializers import BlogSerializer, UserSerializer

User = get_user_model()

class BlogViewset(viewsets.ModelViewSet):
    """Blog viewset"""
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class UserViewset(viewsets.ModelViewSet):
    """User viewset"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

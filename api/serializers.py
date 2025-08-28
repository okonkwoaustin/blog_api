from rest_framework import serializers
from django.contrib.auth import get_user_model
from blogs.models import Blog

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "title",
            "blogger",
            "content",
            "date_created",
            "date_update",
        )
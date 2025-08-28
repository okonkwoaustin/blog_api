from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Blog(models.Model):
    """A blog model"""
    title = models.CharField(max_length=200)
    blogger = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created",)


    def __str__(self):
        """String representation"""
        return self.title


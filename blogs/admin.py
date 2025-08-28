from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'blogger', 'content', 'date_created', 'date_update',
        )
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.blogger = request.user
        super().save_model(request, obj, form, change)
from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    """Administration object for BlogPost models.
    Defines:
     - fields to be displayed in list view (list_display)"""
    list_display = ("title", "author", "post_date")

admin.site.register(BlogPost, BlogPostAdmin)

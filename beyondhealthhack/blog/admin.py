from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ["title", "content", "author",
              "is_published", "has_trigger_warning"]
        })
    ]

admin.site.register(Blog, BlogAdmin)

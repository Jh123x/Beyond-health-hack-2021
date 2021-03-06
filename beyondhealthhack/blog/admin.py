from django.contrib import admin
from .models import Blog, BlogLike


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ["title", "content", "author",
              "is_published", "is_public"]
        })
    ]

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogLike)

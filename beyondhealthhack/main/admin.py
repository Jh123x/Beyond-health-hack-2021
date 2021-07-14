from django.contrib import admin
from .models import ContactUsForm


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ["name", "email", "phone_no", "category", "message"]
        })
    ]

# Register your models here.
admin.site.register(ContactUsForm, ContactAdmin)
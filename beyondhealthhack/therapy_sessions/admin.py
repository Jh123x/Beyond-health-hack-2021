from django.contrib import admin
from .models import TherapySessions, Therapist

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ["start_time", "duration", "in_charge"]
        }),
        ("Meeting Link", {
            'fields': ['link']
        })
    ]

admin.site.register(TherapySessions, SessionAdmin)
admin.site.register(Therapist)
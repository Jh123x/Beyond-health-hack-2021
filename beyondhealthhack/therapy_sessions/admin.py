from django.contrib import admin
from .models import TherapySession, Therapist, Attendance

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ["start_time", "duration", "in_charge", "max_members"]
        }),
        ("Meeting Link", {
            'fields': ['link']
        })
    ]

admin.site.register(TherapySession, SessionAdmin)
admin.site.register(Therapist)
admin.site.register(Attendance)
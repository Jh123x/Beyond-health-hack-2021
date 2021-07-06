from django.db import models
from django.conf import settings
from django.db.models.constraints import CheckConstraint
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model


# Create your models here.
class Therapist(models.Model):
    full_name = models.CharField(max_length=300)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name}"


class TherapySessions(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    link = models.CharField(max_length=200)
    in_charge = models.ForeignKey(Therapist, on_delete=CASCADE)

    def __str__(self):
        return f"{self.start_time}: {self.in_charge}"


class Attendance(models.Model):
    session_id = models.ForeignKey(TherapySessions, on_delete=CASCADE)
    user_id = models.BigIntegerField()

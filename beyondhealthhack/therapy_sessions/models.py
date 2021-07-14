from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Therapist(models.Model):
    full_name = models.CharField(max_length=300)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name}"


class TherapySessions(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    session_title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    link = models.CharField(max_length=200)
    in_charge = models.ForeignKey(Therapist, on_delete=CASCADE)
    max_members = models.IntegerField()

    def __str__(self):
        return f"{self.start_time}: {self.in_charge}"


class Attendance(models.Model):
    session = models.ForeignKey(TherapySessions, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self):
        return f"{self.session}: {self.user.__str__()}"
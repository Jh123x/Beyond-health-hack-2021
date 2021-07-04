from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    likes = models.BigIntegerField()
    views = models.BigIntegerField()

    def __str__(self):
        return f"{self.id}: {self.title}"

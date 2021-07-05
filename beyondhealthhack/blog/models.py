from django.db import models


# Create your models here.
class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    likes = models.BigIntegerField(default=0)
    views = models.BigIntegerField(default=0)
    author = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)
    has_trigger_warning = models.BooleanField(default=False)

    def __str__(self):
        """Representation of the blog as a string"""
        return f"{self.id}: {self.title}"

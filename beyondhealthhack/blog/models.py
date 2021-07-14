from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateField(default=now)
    content = models.CharField(max_length=10000)
    views = models.BigIntegerField(default=0)
    author = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        """Representation of the blog as a string"""
        return f"{self.id}: {self.title}"


class BlogLike(models.Model):
    blog = models.ForeignKey(Blog, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)


class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    blog = models.ForeignKey(Blog, on_delete=CASCADE)
    content = models.CharField(max_length=1000)

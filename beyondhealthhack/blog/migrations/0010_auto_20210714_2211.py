# Generated by Django 3.2.5 on 2021-07-14 14:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_blogcomments_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogComments',
            new_name='BlogComment',
        ),
        migrations.RenameModel(
            old_name='BlogLikes',
            new_name='BlogLike',
        ),
    ]
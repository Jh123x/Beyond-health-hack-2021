# Generated by Django 3.2.5 on 2021-07-08 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_has_trigger_warning_blog_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 20, 46, 44, 624137)),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-10 12:16

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200409_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='image',
            field=models.ImageField(null=True, upload_to=blog.models.upload_blog_image),
        ),
    ]

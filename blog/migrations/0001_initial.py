# Generated by Django 3.0.5 on 2020-04-07 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('author_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('pages', models.IntegerField(default=0)),
                ('cover', models.CharField(choices=[('soft-cover', 'Soft cover'), ('hard-cover', 'Hard cover')], max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
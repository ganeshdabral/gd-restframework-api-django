from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

BOOK_CHOICE = [
    ('soft-cover','Soft cover'),
    ('hard-cover','Hard cover'),
]

def upload_blog_image(instance, filename, **kwargs):
    return f"blog/{instance.user.id}-{instance.slug}-{filename}"


class TestModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to=upload_blog_image, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
@receiver(post_save, sender=TestModel)
def blog_post_save(sender, instance, created, *args, **kwargs):
    if created:
        if instance.title != '' and instance.slug != '':
            instance.slug = slugify(instance.title)
            instance.save()
    return instance
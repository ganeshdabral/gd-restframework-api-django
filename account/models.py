from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def post_save_token(sender, instance, created, *args, **kwargs):
    if created:
        Token.objects.create(user=instance)
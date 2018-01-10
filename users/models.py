from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    RELATION_TO_DENIS_CHOICES = (('H', "Ненависть"), ('U', "Не знаком"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    relation_to_denis = models.CharField(max_length=1, default='H',
                                         choices=RELATION_TO_DENIS_CHOICES)
    ready_to_register = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
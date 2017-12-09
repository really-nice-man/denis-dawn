from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Тема, которую изучает пользователь(название)"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.text

class Entry(models.Model):
    """Информация в теме"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + "..."
        return self.text

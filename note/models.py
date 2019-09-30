from django.db import models
import datetime
from django.contrib.auth.models import User


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.title

# Create your models here.

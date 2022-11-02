from django.db import models

from django.urls import reverse

# Create your models here.


class Activity(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse('addTodo',args=[str(self.id)])

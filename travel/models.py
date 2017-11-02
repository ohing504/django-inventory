from django.contrib.auth.models import User
from django.db import models


class Travel(models.Model):
    title = models.CharField('Title', max_length=127)
    users = models.ManyToManyField(User, blank=True)
    start_date = models.DateTimeField('Start Time', blank=True, null=True)
    end_date = models.DateTimeField('End Time', blank=True, null=True)

    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'

    def __str__(self):
        return self.title

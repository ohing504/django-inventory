from django.db import models


class Travel(models.Model):
    title = models.CharField('Title', max_length=127)

    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'

    def __str__(self):
        return self.title

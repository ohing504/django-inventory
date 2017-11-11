import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from administrator.tasks import import_transaction


class TransactionData(models.Model):
    date = models.DateField(_('Date'), unique=True)
    file = models.FileField(_('File'), upload_to='transaction_data')

    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Transaction Data')
        verbose_name_plural = _('Transaction Data')
        ordering = ['-date']

    def __str__(self):
        return self.date.isoformat()

    @property
    def filename(self):
        return os.path.basename(self.file.name)


@receiver(post_save, sender=TransactionData)
def do_import(sender, instance, created, **kwargs):
    if created:
        import_transaction(instance, instance.file.path)

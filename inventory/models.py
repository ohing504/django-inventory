from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Merchandise(models.Model):
    code = models.CharField(_('Code'), max_length=50, unique=True)
    name = models.CharField(_('Name'), max_length=255)
    category = models.ForeignKey(Category)
    price = models.IntegerField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))
    note = models.TextField(_('Note'), blank=True, null=True)

    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Merchandise')
        verbose_name_plural = _('Merchandises')
        ordering = ['category', 'code']

    def __str__(self):
        return self.name


class Transaction(models.Model):
    merchandise = models.ForeignKey(Merchandise)
    quantity = models.IntegerField(_('Quantity'), default=0)
    date = models.DateField(_('Transaction Date'))

    transaction_data = models.ForeignKey('administrator.TransactionData', blank=True, null=True)

    created_by = models.ForeignKey(User, editable=False, null=True)
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        ordering = ['-date', '-id']

    def __str__(self):
        if self.quantity > 0:
            type_str = 'Buy'
        else:
            type_str = 'Sell'
        return '[{}:{}] {}: {}'.format(self.date, type_str, self.merchandise, abs(self.quantity))

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)

        self.merchandise.quantity += self.quantity
        self.merchandise.save()


@receiver(post_delete, sender=Transaction)
def transaction_post_delete(sender, instance, *args, **kwargs):
    instance.merchandise.quantity -= instance.quantity
    instance.merchandise.save()

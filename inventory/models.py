from django.db import models
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

    def __str__(self):
        return self.name

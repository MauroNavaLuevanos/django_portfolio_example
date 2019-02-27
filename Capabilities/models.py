from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.db.models import FileField
from django.db import models

from colorfield.fields import ColorField

# Create your models here.
__all__ = [
    'CapabilityType',
    'Capability',
    'Service'
]


class CapabilityType(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Capability Type')
        verbose_name_plural = _('Capabilities Types')

    def __str__(self):
        return self.name


class Capability(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    level = models.PositiveSmallIntegerField(
        _('Level'),
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    order = models.PositiveSmallIntegerField(
        unique=True,
        blank=True,
        null=True
    )
    description = models.TextField(_('Description'), blank=True, null=True)
    color = ColorField(default='#007bff')
    type = models.ForeignKey(
        CapabilityType,
        verbose_name=_('Type'),
        on_delete=models.CASCADE,
        related_name=None
    )

    @property
    def get_type(self):
        return self.type.name

    class Meta:
        verbose_name = _('Capability')
        verbose_name_plural = _('Capabilities')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    order = models.IntegerField(_('Order'), unique=True)
    description = models.TextField(_('Description'))
    icon = models.FileField(_('Icon'), upload_to='services')

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    @property
    def get_icon(self):
        return self.icon.url

    def __str__(self):
        return self.name

from django.utils.translation import ugettext_lazy as _
from django.db import models

from colorfield.fields import ColorField

# Create your models here.

class SocialNetwork(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    link = models.URLField(blank=True)
    color = ColorField(default='#6f42c1')
    icon = models.FileField(_('Icon'), upload_to='social')

    @property
    def get_icon(self):
        return self.icon.url

    class Meta:
        verbose_name = _('Social Network')
        verbose_name_plural = _('Social Networks')

    def __str__(self):
        return self.name

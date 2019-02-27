import datetime
import json

from django.utils.translation import ugettext_lazy as _
from django.db import models

from PIL import Image

from Capabilities.models import Capability
from Experiences.models import Company

# Create your models here.

__all__ = [
    'ProjectType',
    'Project'
]


class ProjectType(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Project Type')
        verbose_name_plural = _('Project Types')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'))
    picture = models.ImageField(
        _('Picture'),
        upload_to="portfolio/"
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        on_delete=models.CASCADE,
        related_name=None
    )
    type = models.ForeignKey(
        ProjectType,
        verbose_name=_('Project Type'),
        on_delete=models.CASCADE,
        related_name=None
    )
    date = models.DateField(_('Date'), default=datetime.datetime.today)
    link = models.URLField(blank=True)
    stack = models.ManyToManyField(Capability)

    @property
    def get_type(self):
        return self.type.name

    @property
    def get_company(self):
        return self.company.name

    @property
    def get_picture(self):
        return self.picture.url

    @property
    def get_stack(self):
        return self.stack.values('name', 'color', 'pk')

    @property
    def get_date(self):
        return '{}/{}'.format(self.date.year, self.date.month)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name

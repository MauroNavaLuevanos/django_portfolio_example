import datetime

from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

__all__ = [
    'Experience',
    'Company'
]

class Company(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(_('Position'), max_length=100)
    since = models.DateField(_('Since'), default=datetime.datetime.today)
    until = models.DateField(
        _('Until'),
        default=datetime.datetime.today,
        blank=True,
        null=True
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        on_delete=models.CASCADE,
        related_name=None
    )
    description = models.TextField(_('Description'))

    @property
    def get_company(self):
        return self.company.name

    @property
    def get_timeline(self):
        until = self.until
        timeline_text = '{}/{} - '.format(self.since.month, self.since.year)
        if until:
            timeline_text += '{}/{}'.format(self.until.month, self.until.year)
        else:
            timeline_text += 'present'
        return timeline_text

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')

    def __str__(self):
        return self.company.name

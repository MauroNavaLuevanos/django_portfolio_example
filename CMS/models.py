from django.utils.translation import ugettext_lazy as _
from django.db import models

from solo.models import SingletonModel
from tinymce.models import HTMLField

from Experiences.models import Company

# Create your models here.

__all__ = [
    'CMS'
]

class CMS(SingletonModel):
    # General
    in_development = models.BooleanField(_('In Development'), default=False)
    picture = models.ImageField(_('Picture'), blank=True, null=True, upload_to="CMS")

    # Contact
    email = models.EmailField(blank=True)
    phone = models.CharField(_('Phone'), blank=True, max_length=100)
    cellphone = models.CharField(_('Cellphone'), blank=True, max_length=100)
    city = models.CharField(_('City'), blank=True, max_length=100)
    state = models.CharField(_('State'), blank=True, max_length=100)
    country = models.CharField(_('Country'), blank=True, max_length=100)
    linkedin = models.URLField(blank=True)

    #  Work
    current_work = models.ForeignKey(
        Company,
        verbose_name=_('Current Work'),
        on_delete=models.CASCADE,
        related_name=None,
        blank=True,
        null=True
    )
    work_phone = models.CharField(_('Phone'), blank=True, max_length=100)
    work_city = models.CharField(_('City'), blank=True, max_length=100)
    work_state = models.CharField(_('State'), blank=True, max_length=100)
    work_country = models.CharField(_('Country'), blank=True, max_length=100)
    work_email = models.EmailField(blank=True)

    @property
    def get_company(self):
        return self.current_work.name

    @property
    def get_picture(self):
        return self.picture.url

    @property
    def get_location(self):
        return '{}, {}, {}'.format(self.city, self.state, self.country)

    class Meta:
        verbose_name = 'CMS'

    def __str__(self):
        return 'CMS'

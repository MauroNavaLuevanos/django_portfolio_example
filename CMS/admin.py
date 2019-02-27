from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import CMS

# Register your models here.

@admin.register(CMS)
class CMSAdmin(SingletonModelAdmin):
    fieldsets = (
        (
            _('General'),
            {
                'fields': (
                    'in_development',
                    'picture',
                )
            }
        ),
        (
            _('Contact'),
            {
                'fields': (
                    'email',
                    'phone',
                    'cellphone',
                    'city',
                    'state',
                    'country',
                    'linkedin',
                )
            }
        ),
        (
            _('Work'),
            {
                'fields': (
                    'current_work',
                    'work_phone',
                    'work_city',
                    'work_state',
                    'work_country',
                    'work_email',
                )
            }
        ),
    )

from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(CapabilityType)
class CapabilityTypeTranslation(TranslationOptions):
    fields = (
        'name',
    )


@register(Capability)
class CapabilityTranslation(TranslationOptions):
    fields = (
        'name',
        'description',
    )

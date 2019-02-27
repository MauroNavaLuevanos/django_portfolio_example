from modeltranslation.translator import register, TranslationOptions

from .models import *

@register(ProjectType)
class ProjectTypeTranslation(TranslationOptions):
    fields = (
        'name',
    )


@register(Project)
class ProjectTranslation(TranslationOptions):
    fields = (
        'description',
    )

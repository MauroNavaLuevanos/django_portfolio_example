from modeltranslation.translator import register, TranslationOptions

from .models import Experience

@register(Experience)
class ExperienceTranslation(TranslationOptions):
    fields = (
        'description',
        'position'
    )

from .models import CMS

def cms_processor(request):
    return {
        'CMS': CMS.objects.get()
    }

from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')), # Django Jet
    path('admin/', admin.site.urls),
    path('api/v1/', include('Capabilities.urls')),
    path('api/v1/', include('Experiences.urls')),
    path('api/v1/', include('Social.urls')),
    path('api/v1/', include('Projects.urls')),
    path('api/v1/', include('CMS.urls'))
]

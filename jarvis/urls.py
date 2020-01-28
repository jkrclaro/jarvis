from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework import routers

from .sidefone.urls import router as router_sidefone

admin.autodiscover()
router = routers.DefaultRouter()
router.registry.extend(router_sidefone.registry)
urlpatterns = [
    path('pxdcast/', include('jarvis.pxdcast.urls'), name='pxdcast'),
    path('account/', include('jarvis.accounts.urls'), name='account'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path('__6TJny9S332qv92p57585kZdM9srNA66N2s26M39U4M2232B8Uz/', admin.site.urls),
    ]

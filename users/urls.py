from django.urls import path
from .views import profiles
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', profiles, name='profiles'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
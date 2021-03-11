from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    home_page
)

urlpatterns = [
    path(
            '', home_page, name='home_page'
        ),
    # Add your urls here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
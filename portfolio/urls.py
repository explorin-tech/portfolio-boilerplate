from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    home_page, website, calculator, loginpage, sql
)

urlpatterns = [
    path(
            '', home_page, name='portfolio_home'
        ),
    path(
            'website/', website, name='website'
        ),
    path(
            'calculator/', calculator, name='calculator'
        ),
    path(
            'login_page/', loginpage, name='loginpage'
        ),
    path(
            'sql/', sql, name='sql'
        ),    
    # Add your urls here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
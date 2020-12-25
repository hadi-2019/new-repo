from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include


urlpatterns = i18n_patterns(
    # ...
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('students.urls')),
    path('', include('accounts.urls')),
    # ...

    # If no prefix is given, use the default language
    prefix_default_language=False
)

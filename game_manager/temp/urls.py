from django.conf.urls.defaults import patterns, url, include
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^admin/doc/', include('django.contrib.admindocs.urls')),
  (r'^admin/', include(admin.site.urls)),
  (r'^character\-manager/', include('charon_sheet.character_manager.urls')),
  (r'^game\-manager/', include('charon_sheet.game_manager.urls')),
  (r'^accounts/', include('charon_sheet.accounts.urls')),
  (r'^shortener|g|p/', include('charon_sheet.shortener.urls')),
  (r'^jasmine/', include('jasmine.urls')),
  (r'^', include('charon_sheet.ghosts.urls')),
)

if settings.DEBUG:
  urlpatterns += staticfiles_urlpatterns()

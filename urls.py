from django.conf.urls.defaults import *
from views import character_sheet, list

urlpatterns = patterns(
  '',
  url(r'list/$', 
    view = list,
    name = 'list'
  ),
  url(r'character\-sheet/$', 
    view = character_sheet,
    name = 'character_sheet_new'
  ),
  url(r'character\-sheet/(?P<sheet_id>[0-9]+)/$', 
    view = character_sheet,
    name = 'character_sheet_edit'
  ),
  (r'^logout/$', 'django.contrib.auth.views.logout'),
  (r'', include('django_openid_auth.urls')),  
)

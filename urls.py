from django.conf.urls.defaults import *
from views import character_sheet, list, merit_dots, trait_xp, delete

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
  url(r'character\-sheet/delete/$', 
    view = delete,
    name = 'character_sheet_delete'
  ),
  (r'^logout/$', 'django.contrib.auth.views.logout'),
  (r'', include('django_openid_auth.urls')),
  url(r'merit\-dots/$', 
    view = merit_dots,
    name = 'merit_dots'
  ),
  url(r'trait\-xp/$', 
    view = trait_xp,
    name = 'trait_xp'
  ),
)

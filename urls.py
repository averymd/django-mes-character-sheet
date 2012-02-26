from django.conf.urls.defaults import *
from views import character_sheet_new

urlpatterns = patterns(
  '',
  url(r'character\-sheet/new/$', 
    view = character_sheet_new,
    name = 'character_sheet_new'
  ),  
  (r'', include('django_openid_auth.urls')),  
)

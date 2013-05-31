from django.conf.urls.defaults import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from character_manager import views

urlpatterns = patterns(
  '',
  (r'^logout/$', 'django.contrib.auth.views.logout'),
  (r'', include('django_openid_auth.urls')),  
  url(r'partials/character\-list.html$', 
    view = views.character_list,
  ),
  url(r'partials/character\-detail.html$', 
    view = views.character_detail,
  ),
  url(r'$', 
    view = views.index,
    name = 'character_sheet_index'
  )
)

urlpatterns = format_suffix_patterns(urlpatterns)
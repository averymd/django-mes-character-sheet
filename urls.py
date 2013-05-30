from django.conf.urls.defaults import patterns
from rest_framework.urlpatterns import format_suffix_patterns
from character_manager import views

urlpatterns = patterns(
  '',
  url(r'characters/(?P<pk>[0-9]+)/$', 
    view = views.CharacterDetail.as_view(),
  ),
  (r'^logout/$', 'django.contrib.auth.views.logout'),
  (r'', include('django_openid_auth.urls')),  
  url(r'partials/character\-list.html$', 
    view = views.character_list,
  ),
  url(r'partials/character\-detail.html$', 
    view = views.character_detail,
  ),
  url(r'merit\-dots/$', 
    view = views.merit_dots,
    name = 'merit_dots'
  ),
  url(r'trait\-xp/$', 
    view = views.trait_xp,
    name = 'trait_xp'
  ),
  url(r'$', 
    view = views.index,
    name = 'character_sheet_index'
  )
)

urlpatterns = format_suffix_patterns(urlpatterns)
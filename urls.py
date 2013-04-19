from django.conf.urls.defaults import *
from rest_framework.urlpatterns import format_suffix_patterns
from game_manager import views

urlpatterns = patterns(
  '',
  url(r'factions/(?P<game_id>[0-9]+)/$', views.FactionList.as_view()),
  url(r'games/(?P<game_name>.*?)/(?P<game_id>[0-9]+)/$', views.GameDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
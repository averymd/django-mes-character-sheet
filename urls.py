from django.conf.urls.defaults import *

urlpatterns = patterns(
  '',
  (r'', include('django_openid_auth.urls')),  
)

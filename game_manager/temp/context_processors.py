from charon_sheet.shortener.models import ShortUrl

def sharing_url_context_processor(request):
    if request.path != '/' and 'robots.txt' not in request.path and 'public' not in request.path and 'admin' not in request.path and 'css' not in request.path and 'js' not in request.path and request.method != 'POST':
      app_prefix = 'p'
      long_url = request.get_full_path()[1:] # Losing the initial slash
      try:        
          shortened_url = ShortUrl.objects.get(long_url=long_url, app_prefix=app_prefix)
      except ShortUrl.DoesNotExist:
          shortened_url = ShortUrl.objects.create(long_url=long_url, app_prefix=app_prefix)
      return { 'sharing_url' : shortened_url.short_url(), 'long_url' : shortened_url.full_long_url() }
      
    return { 'sharing_url' : None}

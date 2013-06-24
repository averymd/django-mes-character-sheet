DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'charonsheet',
    'USER': 'averymd',
    'PASSWORD': '80!06o!24',
    'HOST': 'mysql.thecharonsheet.com',
    'PORT': '',
  }
}
MEDIA_ROOT = '/home/averymd/thecharonsheet.com/public/'
MEDIA_URL = '/'
ADMIN_MEDIA_PREFIX = '/admin-static/'
TEMPLATE_DIRS = ('/home/averymd/django/projects/charon_sheet/publish/templates',)
SHORTENER_URL_PREFIX = 'http://thecharonsheet.com/'
EMAIL_HOST = 'localhost'
DEBUG = False
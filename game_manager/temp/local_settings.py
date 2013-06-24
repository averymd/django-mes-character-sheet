MEDIA_URL = '/media/'
STATIC_URL = '/static/'
DEBUG = True
EMAIL_HOST = 'localhost'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'charonsheet.db',        # Or path to database file if using sqlite3.
    'USER': '',                      # Not used with sqlite3.
    'PASSWORD': '',                  # Not used with sqlite3.
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
  }
}

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = 'c:/Users/Melissa/Documents/python/charon_sheet/media/'

SHORTENER_URL_PREFIX = 'http://127.0.0.1:8000/'

STATICFILES_DIRS = (
  'C:/Users/Melissa/Documents/python/charon_sheet/d20_spell_lists/static/',
  'C:/Users/Melissa/Documents/python/charon_sheet/site/',
)

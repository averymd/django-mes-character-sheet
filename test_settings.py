# -*- coding: utf-8 -*-

SECRET_KEY = 'supa_secret'
SITE_ID = 1

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
  }
}

ROOT_URLCONF = 'character_manager.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.request",
  "django.contrib.messages.context_processors.messages",
  
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.admin',

  'character_manager',
  'game_manager',
)

AUTHENTICATION_BACKENDS = (
  "django.contrib.auth.backends.ModelBackend",
)

STATIC_URL = '/static/'
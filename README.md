Django MES Character Sheet
===

MES is the Mind's Eye Society, a group of folks who live action role-play World of Darkness games. This group has been using Excel character sheets for managing characters and XP logs.

We're working on an online version of this system.

It's not ready to be installed or used yet, SO DON'T, unless you want to contribute.

The apps require Python 1.3.1, the Django REST framework, and python-openid.

Quick start
-----------

1. Add "character_manager" and "game_manager" to your INSTALLED_APPS setting like this::

  INSTALLED_APPS = (
  	...
  	'character_manager',
  	'game_manager',
  )

2. Include the polls URLconf in your project urls.py like this::

  url(r'^character\-manager/', include('character_manager.urls')),
  url(r'^game\-manager/', include('game_manager.urls')),

3. Run `python manage.py syncdb` and `python manage.py migratedb` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a game (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/character_manager/ to create and edit characters.

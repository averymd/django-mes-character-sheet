# See http://docs.fabfile.org/en/1.0.1/tutorial.html
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from datetime import datetime

env.user = 'charonsheet'
env.hosts = ['thecharonsheet.com']

def test():
  local("python manage.py test shortener ghosts")

def commit():
  with settings(warn_only=True):
    result = local("git commit -as", capture=True)
  if result.failed and not confirm("Commit failed. Continue anyway?"):
    abort("Aborting at user request.")
  else:  
    local("git push")

def build():
  with lcd('build'):
    local('runbuildscript.bat')
    
def prepare_deploy():
  test()
  #build()
  commit()

def initial_deploy(branch='master'):
  code_dir = '/home/charonsheet/django/projects'
  domain_dir = '/home/charonsheet/thecharonsheet.com'
  project = 'charon_sheet'
  repo = 'http://averymd:0233235@projects.irrsinn.net/git/charon_sheet.git'
  with cd(code_dir):
    run("git clone %s %s" % (repo, project))
  with cd(code_dir + '/' + project):
    run("git checkout %s" % branch)
    local_settings()
    #run('ln -s /home/charonsheet/env/lib/python2.5/site-packages/Django-1.3-py2.5.egg/django/contrib/admin/media publish/public/admin-static')
    # with settings(warn_only=True):
        # # This is going to fail on account of mySQL being unable to handle 
        # # indexes with TEXT fields when there aren't limits on the index size.
        # # So we run syncdb, let it fail, and then create the Shortener table ourself.
        # result = run('python manage.py syncdb')
    # if result.failed:
        # prompt("Syncdb failed. You need to create the ShortUrl table manually and add the index with alter table shortener_shorturl add unique index (long_url(300), `app_prefix`). Continue?")
  with cd(domain_dir):
    run("ln -s %s/%s/publish/public" % (code_dir, project))
    run('ln -s %s/%s/remote_passenger_wsgi.py passenger_wsgi.py' % (code_dir, project))
  
def deploy(branch='master'):
  code_dir = '/home/charonsheet/django/projects/charon_sheet'
  prepare_deploy()
  with cd(code_dir):
    run('git reset --hard')
    run("git pull")
    run('git checkout %s' % (branch))
    local_settings()
  restart_remote()
    
def local_settings():
  code_dir = '/home/charonsheet/django/projects/charon_sheet'
  with cd(code_dir):    
    run('rm local_settings.py')
    run('ln -s remote_local_settings.py local_settings.py')
  
def restart_remote():
  domain_dir = '/home/charonsheet/thecharonsheet.com'
  with cd(domain_dir):
    run('touch tmp/restart.txt')

def send_up_content():
  code_dir = '/home/charonsheet/django/projects/charon_sheet/backups/'
  current_ts = datetime.now().strftime('%Y%m%d-%H%M%S%z')
  local('python manage.py dumpdata flatpages --indent=2 > backups/%s-backup-flatpages.json' % (current_ts))
  local('git add backups/*')
  deploy()
  with cd(code_dir):
    run('python ../manage.py loaddata %s-backup-flatpages.json' % (current_ts))
  
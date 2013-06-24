import sys, os
INTERP = "/home/averymd/env/bin/python"
#INTERP is present twice so that the new python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
sys.path.insert(1, "/home/averymd/django/projects")
sys.path.insert(1, os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'charon_sheet.settings'
import django.core.handlers.wsgi
from paste.exceptions.errormiddleware import ErrorMiddleware
application = django.core.handlers.wsgi.WSGIHandler()
# To cut django out of the loop, comment the above application = ... line ,
# and remove "test" from the below function definition.
def testapplication(environ, start_response):
    status = '200 OK'
    output = 'Hello World! Running Python version ' + sys.version + '\n\n'
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    # to test paste's error catching prowess, uncomment the following line
    # while this function is the "application"
    raise("error")
    start_response(status, response_headers)    
    return [output]

application = ErrorMiddleware(application, debug=False)

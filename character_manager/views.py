from django.shortcuts import render_to_response
#from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
#from django.conf import settings
#from django.contrib import messages

@login_required
def index(request):  
  return render_to_response('character_manager/index.html', {'page_title' : 'Character Sheets', 'page_name' : 'charsheets'},
    context_instance=RequestContext(request))

@login_required
def character_list(request):  
  return render_to_response('character_manager/partials/character-list.html',
    context_instance=RequestContext(request))

@login_required
def character_detail(request):  
  return render_to_response('character_manager/partials/character-detail.html',
    context_instance=RequestContext(request))
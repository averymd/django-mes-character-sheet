from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.template import RequestContext
from forms import GeistCharacterSheetForm
from django.conf import settings

def character_sheet_new(request):
  form = GeistCharacterSheetForm()
  
  return render_to_response('character_manager/character_sheet.html', { 'form' : form, 'page_title' : 'New Character Sheet', 'page_name' : 'charsheetform' },
    context_instance=RequestContext(request))
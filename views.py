from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.template import RequestContext
from models import GeistCharacterSheet, ChosenTrait, XpEntry, XpLog, Character
from game_manager.models import Trait
from forms import GeistCharacterSheetForm, ChosenAttributeSkillForm, ChosenSkillForm, ChosenMeritForm, XpEntryForm
from character_manager.serializers import CharacterSerializer
from django.conf import settings
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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
    
@login_required
def merit_dots(request):
  if request.method == 'POST' and request.is_ajax():
    if request.POST['merit-id'].isdigit():
      try:
        merit = Trait.objects.get(pk=int(request.POST['merit-id']), trait_type__name='Merit')
        values, dots = zip(*merit.available_dots())
        json_dots = json.dumps({ 'dots' : values })
        return HttpResponse(json_dots, mimetype='text/json')
      except Trait.DoesNotExist:
        raise ValueError
    else:
      raise TypeError
  
  return HttpResponseForbidden()
  
@login_required
def trait_xp(request):
  if request.method == 'POST' and request.is_ajax():
    if request.POST['trait-id'].isdigit() and request.POST['character-id'].isdigit() and request.POST['new-level'].isdigit():
      try:
        trait = Trait.objects.get(pk=int(request.POST['trait-id']))
        character = GeistCharacterSheet.objects.get(pk=int(request.POST['character-id']), user=request.user)
        new_level = int(request.POST['new-level'])
        values, dots = zip(*trait.available_dots())
        code, type = zip(*XpLog.category_options)
        if new_level in values:
          json_xp = json.dumps({ 'xpchange' : character.cost_for_trait_change(trait, new_level), 'types' : dict(zip(type, code)) })
          return HttpResponse(json_xp, mimetype='text/json')
      except Trait.DoesNotExist, GeistCharacterSheet.DoesNotExist:
        raise ValueError
    else:
      raise TypeError
  
  return HttpResponseForbidden()
        
def setup_attribute_form(charsheet, post=None):
  AttributeFormSet = inlineformset_factory(GeistCharacterSheet, ChosenTrait, form=ChosenAttributeSkillForm, can_delete=False, extra=0)
  if post:
    return AttributeFormSet(post, instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Attribute'), prefix='attribute')
  else:
    return AttributeFormSet(instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Attribute'), prefix='attribute')
  
def setup_merit_form(charsheet, post=None):
  MeritFormSet = inlineformset_factory(GeistCharacterSheet, ChosenTrait, form=ChosenMeritForm, extra=1)
  if post:
    forms = MeritFormSet(post, instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Merit'), prefix='merit')
  else:
    forms = MeritFormSet(instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Merit'), prefix='merit')
  return forms

def setup_skill_form(charsheet, post=None):
  SkillFormSet = inlineformset_factory(GeistCharacterSheet, ChosenTrait, form=ChosenSkillForm, can_delete=False, extra=0)
  if post:
    return SkillFormSet(post, instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Skill'), prefix='skill')
  else:
    return SkillFormSet(instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Skill'), prefix='skill')
    
def setup_xplog_form(charsheet, post=None):
  XPLogFormSet = inlineformset_factory(XpLog, XpEntry, form=XpEntryForm, extra=1)
  if post:
    return XPLogFormSet(post, instance=charsheet.xp_log, prefix='xplog')
  else:
    return XPLogFormSet(instance=charsheet.xp_log, prefix='xplog')
    
class CharacterDetail(APIView):
  """
  Retrieve, update or delete a character instance.
  """
  def get_object(self, pk):
    try:
      return Character.objects.get(pk=pk)
    except Character.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    character = self.get_object(pk)
    serializer = CharacterSerializer(character)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    character = self.get_object(pk)
    serializer = CharacterSerializer(character, data=request.DATA)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    character = self.get_object(pk)
    character.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
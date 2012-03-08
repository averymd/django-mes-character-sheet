from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.template import RequestContext
from models import GeistCharacterSheet, ChosenTrait, XpEntry, XpLog
from game_manager.models import Trait
from forms import GeistCharacterSheetForm, ChosenAttributeSkillForm, ChosenSkillForm, ChosenMeritForm
from django.conf import settings
from django.contrib import messages
import json

def list(request):
  if request.user.is_authenticated():
    charsheets = GeistCharacterSheet.objects.filter(user=request.user)
    
    return render_to_response('character_manager/list.html', {'character_sheets' : charsheets, 'page_title' : 'Character Sheets', 'page_name' : 'charsheets'},
      context_instance=RequestContext(request))

def character_sheet(request, sheet_id=None):
  if request.user.is_authenticated():
    if sheet_id is not None:
      try:
        charsheet = GeistCharacterSheet.objects.get(pk=sheet_id, user=request.user)
        if request.method == 'POST':
          sheet_form = GeistCharacterSheetForm(request.POST, instance=charsheet)          
          attribute_formset = setup_attribute_form(charsheet, post=request.POST)
          skill_formset = setup_skill_form(charsheet, post=request.POST)
          merit_formset = setup_merit_form(charsheet, post=request.POST)
          xplog_formset = setup_xplog_form(charsheet, post=request.POST)
          
          if sheet_form.is_valid() and attribute_formset.is_valid() and skill_formset.is_valid() and merit_formset.is_valid() and xplog_formset.is_valid():
            sheet_form.save()
            attribute_formset.save()
            skill_formset.save()
            merit_formset.save()
            xplog_formset.save()
            return redirect('/character-manager/list/')
        else:
          sheet_form = GeistCharacterSheetForm(instance=charsheet)          
          attribute_formset = setup_attribute_form(charsheet)
          skill_formset = setup_skill_form(charsheet)
          merit_formset = setup_merit_form(charsheet)
          xplog_formset = setup_xplog_form(charsheet)
        
        return render_to_response('character_manager/character_sheet.html', {
          'charsheet' : charsheet,
          'sheet_form' : sheet_form, 
          'attribute_formset' : attribute_formset, 
          'skill_formset' : skill_formset, 
          'merit_formset' : merit_formset,
          'xplog_formset' : xplog_formset,
          'page_title' : 'New Character Sheet', 
          'page_name' : 'charsheetform' }, 
          context_instance=RequestContext(request))
      except GeistCharacterSheet.DoesNotExist:
        messages.error(request, 'That character sheet doesn\'t exist.')
        return redirect(list)
    else:
      if request.method == 'POST':
        sheet_form = GeistCharacterSheetForm(request.POST)
        if sheet_form.is_valid():
          sheet = sheet_form.save(commit=False)
          sheet.user = request.user
          sheet.save()
          return redirect(sheet.get_absolute_url())
      else:
        sheet_form = GeistCharacterSheetForm()        
        return render_to_response('character_manager/character_sheet.html', { 'sheet_form' : sheet_form, 'page_title' : 'New Character Sheet', 'page_name' : 'charsheetform' }, context_instance=RequestContext(request))

def merit_dots(request):
  if request.user.is_authenticated() and request.method == 'POST' and request.is_ajax():
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
  
def trait_xp(request):
  if request.user.is_authenticated() and request.method == 'POST' and request.is_ajax():
    if request.POST['trait-id'].isdigit() and request.POST['character-id'].isdigit() and request.POST['new-level'].isdigit():
      try:
        trait = Trait.objects.get(pk=int(request.POST['trait-id']))
        character = GeistCharacterSheet.objects.get(pk=int(request.POST['character-id']), user=request.user)
        new_level = int(request.POST['new-level'])
        values, dots = zip(*trait.available_dots())
        if new_level in values:
          json_xp = json.dumps({ 'xpchange' : character.cost_for_trait_change(trait, new_level) })
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
    return MeritFormSet(post, instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Merit'), prefix='merit')
  else:
    return MeritFormSet(instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Merit'), prefix='merit')  

def setup_skill_form(charsheet, post=None):
  SkillFormSet = inlineformset_factory(GeistCharacterSheet, ChosenTrait, form=ChosenSkillForm, can_delete=False, extra=0)
  if post:
    return SkillFormSet(post, instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Skill'), prefix='skill')
  else:
    return SkillFormSet(instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Skill'), prefix='skill')
    
def setup_xplog_form(charsheet, post=None):
  XPLogFormSet = inlineformset_factory(XpLog, XpEntry, extra=1)
  if post:
    return XPLogFormSet(post, instance=charsheet.xp_log, prefix='xplog')
  else:
    return XPLogFormSet(instance=charsheet.xp_log, prefix='xplog')
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.template import RequestContext
from models import GeistCharacterSheet, ChosenTrait
from game_manager.models import Trait
from forms import GeistCharacterSheetForm, ChosenAttributeSkillForm, ChosenSkillForm
from django.conf import settings
from django.contrib import messages


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
        sheet_form = GeistCharacterSheetForm(instance=charsheet)
        attribute_trait_formset = setup_attribute_form(charsheet)
        skill_trait_formset = setup_skill_form(charsheet)
        
        return render_to_response('character_manager/character_sheet.html', { 'sheet_form' : sheet_form, 'attribute_trait_formset' : attribute_trait_formset, 'skill_trait_formset' : skill_trait_formset, 'page_title' : 'New Character Sheet', 'page_name' : 'charsheetform' }, context_instance=RequestContext(request))
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
        
def setup_attribute_form(charsheet):
  AttributeFormSet = inlineformset_factory(GeistCharacterSheet, ChosenTrait, form=ChosenAttributeSkillForm, can_delete=False, extra=0)
  return AttributeFormSet(instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Attribute'), prefix='attribute')
  
def setup_skill_form(charsheet):
  SkillFormSet = inlineformset_factory(GeistCharacterSheet, ChosenTrait, form=ChosenSkillForm, can_delete=False, extra=0)
  return SkillFormSet(instance=charsheet, queryset=ChosenTrait.objects.filter(trait__trait_type__name='Skill'), prefix='skill')
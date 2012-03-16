from django.forms import ModelForm, HiddenInput, IntegerField, CharField, ChoiceField, Select, ModelChoiceField, RadioSelect, Textarea
from character_manager.models import GeistCharacterSheet, ChosenTrait, XpLog, XpEntry
from game_manager.models import Geist, Trait, Faction, Subrace
from widgets import DotRenderer

class GeistCharacterSheetForm(ModelForm):  
  dob = CharField(label='Date of Birth', required=False)
  
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(GeistCharacterSheetForm, self).__init__(*args, **kwargs)
    game = Geist.objects.get(pk=1)
    self.fields['faction'].label = '%s' % (game.faction_name)
    self.fields['subrace'].label='%s' % (game.subrace_name)
    self.fields['coordinator_name'].initial = self.user.profile.coordinator_name
    self.fields['coordinator_email'].initial = self.user.profile.coordinator_email
  
  class Meta:
    model = GeistCharacterSheet
    exclude = ('xp_log, is_active')
    
class ChosenAttributeSkillForm(ModelForm):   
  def __init__(self, *args, **kwargs):
    super(ChosenAttributeSkillForm, self).__init__(*args, **kwargs)
    self.fields['level'] = ChoiceField(label=u'%s' % (self.instance.trait.name), required=True, choices=self.instance.trait.available_dots(), widget=RadioSelect())
    self.fields['trait'] = ModelChoiceField(queryset=Trait.objects.filter(trait_type__name='Attribute'), widget=HiddenInput())
    
  class Meta:
    model = ChosenTrait
    exclude = ('specializations')
    
class ChosenSkillForm(ChosenAttributeSkillForm):
  def __init__(self, *args, **kwargs):
    super(ChosenAttributeSkillForm, self).__init__(*args, **kwargs)
    self.fields['level'] = ChoiceField(label=u'%s' % (self.instance.trait.name), required=False, choices=self.instance.trait.available_dots(), widget=RadioSelect())
    self.fields['trait'] = ModelChoiceField(queryset=Trait.objects.filter(trait_type__name='Skill'),widget=HiddenInput())
    
  class Meta(ChosenAttributeSkillForm.Meta):
    exclude = ()

class ChosenMeritForm(ModelForm):   
  def __init__(self, *args, **kwargs):
    super(ChosenMeritForm, self).__init__(*args, **kwargs)
    self.fields['specializations'].label = u'Details'
    self.fields['trait'] = ModelChoiceField(required=True, queryset=Trait.objects.filter(trait_type__name='Merit'))
    self.fields['level'] = ChoiceField(choices=Trait.LEVEL_CHOICES, widget=RadioSelect(renderer=DotRenderer), label=u'Merit')
    
    try: 
      self.fields['level'].widget.renderer.actives = self.active_dots()
    except Trait.DoesNotExist:
      pass #del self.fields['level'].widget.renderer.actives
    
  def active_dots(self):
    self.available_dots = []
    for dot in Trait.LEVEL_CHOICES:
      print "%s's available dots" % (self.instance.trait)
      print self.instance.trait.available_dots()
      if dot not in self.instance.trait.available_dots():
        self.available_dots.append(False)
      else:
        self.available_dots.append(True)
    print 'no exception for %s' % (self.instance.trait)
    print 'all dots after all changes'
    print self.available_dots
    return self.available_dots
    
  class Meta:
    model = ChosenTrait
        
class XpLogForm(ModelForm):
  class Meta:
    model = XpLog
    
class XpEntryForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(XpEntryForm, self).__init__(*args, **kwargs)
    self.fields['details'].widget = Textarea(attrs={'rows': '2', 'cols':'30'})
    
  class Meta:
    model = XpEntry
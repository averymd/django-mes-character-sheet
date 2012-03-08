from django.forms import ModelForm, HiddenInput, IntegerField, CharField, ChoiceField, Select, ModelChoiceField, RadioSelect
from character_manager.models import GeistCharacterSheet, ChosenTrait, XpLog, XpEntry
from game_manager.models import Geist, Trait, Faction, Subrace

class GeistCharacterSheetForm(ModelForm):  
  dob = CharField(label='Date of Birth', required=False)
  
  def __init__(self, *args, **kwargs):
    super(GeistCharacterSheetForm, self).__init__(*args, **kwargs)
    game = Geist.objects.get(pk=1)
    self.fields['faction'].label = '%s' % (game.faction_name)
    self.fields['subrace'].label='%s' % (game.subrace_name)
  
  class Meta:
    model = GeistCharacterSheet
    exclude = ('xp_log')
    
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
    self.fields['trait'].label = u'Merit'
    try:
      self.fields['level'] = ChoiceField(choices=self.instance.trait.available_dots(), 
        widget=RadioSelect())
    except Trait.DoesNotExist:
      self.fields['level'] = ChoiceField(choices=Trait.LEVEL_CHOICES, 
        widget=RadioSelect())
    
  class Meta:
    model = ChosenTrait
        
class XpLogForm(ModelForm):
  class Meta:
    model = XpLog
    
class XpEntryForm(ModelForm):
  class Meta:
    model = XpEntry
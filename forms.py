from django.forms import ModelForm, HiddenInput, IntegerField, CharField, ChoiceField
from character_manager.models import GeistCharacterSheet, ChosenTrait, XpLog, XpEntry
from game_manager.models import Geist, Faction, Subrace

class GeistCharacterSheetForm(ModelForm):
  
  dob = CharField(label='Date of Birth')
  
  def __init__(self, *args, **kwargs):
    super(GeistCharacterSheetForm, self).__init__(*args, **kwargs)
    game = Geist.objects.get(pk=1)
    faction = ChoiceField(label=u'%s' % (game.faction_name), choices=[(f.id, u'%s' % (f.name)) for f in game.factions.all()])
    subrace = ChoiceField(label=u'%s' % (game.subrace_name), choices=[(s.id, u'%s' % (s.name)) for s in game.subraces.all()])
  
  class Meta:
    model = GeistCharacterSheet
    exclude = ('xp_log')
    
class ChosenTraitForm(ModelForm):  
  # def __init__(self, trait, *args, **kwargs):
    # super(ChosenTraitForm, self).__init__(*args, **kwargs)
    # self.fields['trait'] = forms.HiddenField(widget=HiddenInput(attr={'value':trait.id}))
    # self.fields['level'] = forms.IntegerField(label=trait.name)
    
  class Meta:
    model = ChosenTrait
    
class XpLogForm(ModelForm):
  class Meta:
    model = XpLog
    
class XpEntryForm(ModelForm):
  class Meta:
    model = XpEntry
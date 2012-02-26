from django.forms import ModelForm
from character_manager.models import GeistCharacterSheet

class GeistCharacterSheetForm:
  class Meta:
    model = GeistCharacterSheet
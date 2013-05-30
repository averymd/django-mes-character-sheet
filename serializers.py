from rest_framework import serializers
from character_manager.models import Character
#from game_manager.models import Trait, Game, Geist, Faction, Subrace

class CharacterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Character
    fields = ('name', 'concept', 'age', 'dob', 'virtue', 'vice', 'mc_level_at_creation')

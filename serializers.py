from rest_framework import serializers
from game_manager.models import Trait, Game, Geist, Faction, Subrace, Power, GEIST_XP_CATEGORY_OPTIONS

class FactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Faction
    fields = ('id', 'name')
    
class SubraceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subrace
    fields = ('id', 'name')

class TraitSerializer(serializers.ModelSerializer):
  category = serializers.ChoiceField(choices=Trait.CATEGORY_OPTIONS, default='friendly')
  
  class Meta:
    model = Trait
    fields = ('id', 'name', 'category', 'use', 'specific_dots', 'trait_type', 'uses_simple_calculation', 'custom_xp_per_dot')
  
class GeistSerializer(serializers.ModelSerializer):
  morality = serializers.RelatedField()
  power_level_trait = TraitSerializer()
  keys = TraitSerializer(many=True)
  merits = TraitSerializer(many=True)
  skills = TraitSerializer(many=True)
  xp_category_options = serializers.Field(source='XP_CATEGORY_OPTIONS')
  
  class Meta:
    model = Geist
    fields = ('id', 'name', 'subrace_name', 'faction_name', 'energy_name', 'power_level_trait', 'keys', 'morality', 'merits', 'skills', 'xp_category_options')
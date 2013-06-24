from rest_framework import serializers
from game_manager.models import Trait, Geist, Faction, Subrace, TraitType

class FactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Faction
    fields = ('id', 'name')
    
class SubraceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subrace
    fields = ('id', 'name')
    
class TraitTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = TraitType
    fields = ('id', 'name', 'default_xp_cost_per_dot')

class TraitSerializer(serializers.ModelSerializer):
  category = serializers.ChoiceField(choices=Trait.CATEGORY_OPTIONS, default='friendly')
  trait_type = TraitTypeSerializer()
  
  class Meta:
    model = Trait
    fields = ('id', 'name', 'category', 'use', 'specific_dots', 'trait_type', 'uses_simple_calculation', 'custom_xp_per_dot')
    
class GeistSerializer(serializers.ModelSerializer):
  morality = serializers.RelatedField()
  power_level_trait = TraitSerializer()
  keys = TraitSerializer(many=True)
  merits = TraitSerializer(many=True)
  skills = TraitSerializer(many=True)
  attributes = TraitSerializer(many=True)
  xp_category_options = serializers.Field(source='XP_CATEGORY_OPTIONS')
  
  class Meta:
    model = Geist
    fields = ('id', 'name', 'subrace_name', 'faction_name', 'energy_name', 'power_level_trait', 'keys', 'morality', 'attributes', 'merits', 'skills', 'xp_category_options')
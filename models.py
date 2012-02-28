from django.db import models

class TraitType(models.Model):
  name = models.CharField(max_length=100)
  default_xp_cost_per_dot = models.IntegerField()
  
  def __unicode__(self):
    return self.name

class Trait(models.Model):
  category_options = ((1, 'Mental'), (2, 'Physical'), (3, 'Social'))
  use_options = ((1, 'Power'), (2, 'Finesse'), (3, 'Resistance'))
  
  name = models.CharField(max_length=100)
  category = models.IntegerField(choices=category_options, blank=True, null=True)
  use = models.IntegerField(choices=use_options, blank=True, null=True)
  specific_dots = models.CharField(max_length=10, blank=True)
  trait_type = models.ForeignKey(TraitType)
  uses_simple_calculation = models.BooleanField()
  custom_xp_per_dot = models.IntegerField(blank=True, null=True)
  
  def __unicode__(self):
    return self.name
    
  class Meta:
    ordering = ['trait_type', 'category' , 'use' , 'name']
    
class Game(models.Model):  
  name = models.CharField(max_length=200)
  subrace_name = models.CharField(max_length=200)
  faction_name = models.CharField(max_length=200)
  energy_name = models.CharField(max_length=200)
  power_level_trait = models.ForeignKey(Trait, related_name='power_level_trait', limit_choices_to={'trait_type__name':'Advantage'})
  morality = models.ForeignKey(Trait, related_name='morality', limit_choices_to={'trait_type__name':'Advantage'})
  willpower = models.ForeignKey(Trait, related_name='willpower', limit_choices_to={'trait_type__name':'Advantage'})
  attributes = models.ManyToManyField(Trait, related_name='attributes', limit_choices_to={'trait_type__name':'Attribute'})
  merits = models.ManyToManyField(Trait, related_name='merits', limit_choices_to={'trait_type__name':'Merit'})
  skills = models.ManyToManyField(Trait, related_name='skills', limit_choices_to={'trait_type__name':'Skill'})
  
  vice_options = ((1, 'Envy'), (2, 'Gluttony'), (3, 'Greed'), (4, 'Lust'), (5, 'Pride'), (6, 'Sloth'), (7, 'Wrath'))
  virtue_options = ((1, 'Charity'), (2, 'Faith'), (3, 'Fortitude'), (4, 'Hope'), (5, 'Justice'), (6, 'Prudence'), (7, 'Temperance'))
  
  def __unicode__(self):
    return self.name
  
  class Meta:
    abstract = True

class Geist(Game):
  keys = models.ManyToManyField(Trait, related_name='keys', limit_choices_to={'trait_type__name':'Key'})

class Subrace(models.Model):
  name = models.CharField(max_length=100)
  game = models.ForeignKey(Geist, related_name='subraces')
  
  def __unicode__(self):
    return self.name
    
class Faction(models.Model):
  name = models.CharField(max_length=100)
  game = models.ForeignKey(Geist, related_name='factions')
  
  def __unicode__(self):
    return self.name
  
class Power(models.Model):
  name = models.CharField(max_length=100)
  xp_cost_per_dot = models.IntegerField()
  activation_traits = models.ManyToManyField(Trait, related_name='+')
  game = models.ForeignKey(Geist, related_name='powers')
  
  def __unicode__(self):
    return self.name
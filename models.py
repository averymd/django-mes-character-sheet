from django.db import models

GEIST_XP_CATEGORY_OPTIONS = ((1, 'Game Attendance'), 
    (2, 'Attribute'), 
    (3, 'Merit'), 
    (4, 'Skill'),
    (5, 'Skill Specialization'),
    (6, 'Key'),
    (7, 'Willpower'),
    (8, 'Downtime'),
    (9, 'Creation Attribute'),
    (10, 'Creation Merit'),
    (11, 'Creation Skill'),
    (12, 'Creation Skill Specialization'),
  )
  
class TraitType(models.Model):
  name = models.CharField(max_length=100)
  default_xp_cost_per_dot = models.IntegerField()
  
  def __unicode__(self):
    return self.name

class Trait(models.Model):
  CATEGORY_OPTIONS = ((1, 'Mental'), (2, 'Physical'), (3, 'Social'))
  use_options = ((1, 'Power'), (2, 'Finesse'), (3, 'Resistance'))
  
  name = models.CharField(max_length=100)
  category = models.IntegerField(choices=CATEGORY_OPTIONS, blank=True, null=True)
  use = models.IntegerField(choices=use_options, blank=True, null=True)
  specific_dots = models.CharField(max_length=10, blank=True)
  trait_type = models.ForeignKey(TraitType)
  uses_simple_calculation = models.BooleanField()
  custom_xp_per_dot = models.IntegerField(blank=True, null=True)
  
  LEVEL_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
  SKILL_LEVEL_CHOICES = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
  
  def available_dots(self):
    try:
      if self.specific_dots != '':
        level_choices = tuple((int(i), str(i)) for i in self.specific_dots.split(','))
      else:
        if self.trait_type.name == 'Skill':
          level_choices = Trait.SKILL_LEVEL_CHOICES
        else:
          level_choices = Trait.LEVEL_CHOICES
    except Trait.DoesNotExist:
      level_choices = Trait.LEVEL_CHOICES
    
    return level_choices
      
  def cost_for_trait_change(self, old_level, new_level):
    cost = 0
    if self.uses_simple_calculation:
      if self.custom_xp_per_dot is not None:
        if (old_level < new_level):
          cost = new_level * self.custom_xp_per_dot
        else:
          cost = (new_level - old_level) * self.custom_xp_per_dot
      else:
        if (old_level < new_level):
          cost = new_level * self.trait_type.default_xp_cost_per_dot
        else:
          cost = (new_level - old_level) * self.trait_type.default_xp_cost_per_dot
    else:
      if self.custom_xp_per_dot is not None:
        if (old_level < new_level):
          cost = sum([i * self.custom_xp_per_dot for i in range(old_level+1, new_level+1)])
        else:
          cost = -1*sum([i * self.custom_xp_per_dot for i in range(new_level+1, old_level+1)])
      else:
        if (old_level < new_level):
          cost = sum([i * self.trait_type.default_xp_cost_per_dot for i in range(old_level+1, new_level+1)])
        else:
          cost = -1*sum([i * self.trait_type.default_xp_cost_per_dot for i in range(new_level+1, old_level+1)])
  
    return -1*cost    
  
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
  XP_CATEGORY_OPTIONS = ((1, 'Game Attendance'), 
    (2, 'Attribute'), 
    (3, 'Merit'), 
    (4, 'Skill'),
    (5, 'Skill Specialization'),
    (6, 'Key'),
    (7, 'Willpower'),
    (8, 'Downtime'),
    (9, 'Creation Attribute'),
    (10, 'Creation Merit'),
    (11, 'Creation Skill'),
    (12, 'Creation Skill Specialization'),
  )

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
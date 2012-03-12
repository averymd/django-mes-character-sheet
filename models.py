from django.db import models
from django.db.models import Sum
from datetime import datetime
from django.contrib.auth.models import User
from game_manager.models import Trait, Game, Geist, Faction, Subrace
from math import fabs
    
class XpLog(models.Model):
  category_options = ((1, 'Game'), (2, 'Attribute'), (3, 'Merit'), (4, 'Downtime'), (5, 'Skill'))
  
  def xp_earned(self):
    return self.xpentry_set.filter(xp_change__gt=0).aggregate(total_earned=Sum('xp_change'))['total_earned']
    
  def xp_remaining(self):
    return self.xpentry_set.aggregate(total_remaining=Sum('xp_change'))['total_remaining']
  
  def xp_spent(self):
    return int(fabs(self.xpentry_set.filter(xp_change__lt=0).aggregate(total_spent=Sum('xp_change'))['total_spent']))

class XpEntry(models.Model):
  date = models.DateField()
  category = models.IntegerField(choices=XpLog.category_options, max_length=100)
  xp_change = models.IntegerField()
  details = models.TextField(blank=True)
  xp_log = models.ForeignKey(XpLog, editable=False)
  
class CharacterSheet(models.Model):
  name = models.CharField(max_length=100, default='New Sin-Eater')
  concept = models.CharField(max_length=400, blank=True)
  age = models.CharField(max_length=100, blank=True)
  dob = models.CharField(max_length=100, blank=True)
  virtue = models.IntegerField(choices=Game.virtue_options, blank=True, null=True)
  vice = models.IntegerField(choices=Game.vice_options, blank=True, null=True)
  mc_level_at_creation = models.IntegerField(blank=True, null=True)
  primary_character = models.BooleanField(blank=True)
  storyteller_name = models.CharField(max_length=100, blank=True)
  storyteller_email = models.EmailField(blank=True)
  coordinator_name = models.CharField(max_length=200, blank=True)
  coordinator_email = models.EmailField(blank=True)
  is_active = models.BooleanField(default=True)
  xp_log = models.OneToOneField(XpLog)
  user = models.ForeignKey(User, editable=False)
  
  created_at = models.DateTimeField(default=datetime.now, editable=False)
  updated_at = models.DateTimeField(auto_now=True)
  
  def save(self, *args, **kwargs):
    try:
      self.xp_log
    except XpLog.DoesNotExist:
      self.xp_log = XpLog.objects.create()
    super(CharacterSheet, self).save(*args, **kwargs) # Call the "real" save() method.
  
  def xp_earned(self):
    return self.xp_log.xp_earned()
  
  def xp_remaining(self):
    return self.xp_log.xp_remaining()
    
  def xp_spent(self):
    return self.xp_log.xp_spent()
    
  def __unicode__(self):
    return u'%s' % (self.name)

  class Meta:
    abstract = True
    
class GeistCharacterSheet(CharacterSheet):
  faction = models.ForeignKey(Faction, blank=True, null=True)
  subrace = models.ForeignKey(Subrace, blank=True, null=True)
  
  def cost_for_trait_change(self, trait, new_level):
    try:
      old_level = self.chosentrait_set.get(trait=trait).level
    except ChosenTrait.DoesNotExist:
      old_level = 0 # Probably a merit-ish thing.
    return trait.cost_for_trait_change(old_level=old_level, new_level=new_level)
    
  @models.permalink
  def get_absolute_url(self):
    return ('character_sheet_edit', (), {'sheet_id':str(self.id)})
  
  def save(self, *args, **kwargs):
    super(GeistCharacterSheet, self).save(*args, **kwargs) # Call the "real" save() method.
    if not self.chosentrait_set.filter(trait__trait_type__name='Attribute').exists():
      for attribute in Trait.objects.filter(trait_type__name='Attribute'):
        self.chosentrait_set.create(trait=attribute, level=1)
        
    if not self.chosentrait_set.filter(trait__trait_type__name='Skill').exists():
      for attribute in Trait.objects.filter(trait_type__name='Skill'):
        self.chosentrait_set.create(trait=attribute, level=0)
  
class ChosenTrait(models.Model):
  trait = models.ForeignKey(Trait)
  level = models.IntegerField(default=0, blank=True, null=True)
  character = models.ForeignKey(GeistCharacterSheet, editable=False)
  specializations = models.CharField(max_length=300, blank=True)
  created_at = models.DateTimeField(default=datetime.now, editable=False)
  updated_at = models.DateTimeField(auto_now=True)
    
  def __unicode__(self):
    return u'%s at %s dots' % (self.trait, str(self.level))

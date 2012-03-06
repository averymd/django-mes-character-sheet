from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from game_manager.models import Trait, Game, Geist, Faction, Subrace
    
class XpLog(models.Model):
  category_options = ((1, 'Game'), (2, 'Attribute'), (3, 'Merit'), (4, 'Downtime'))

class XpEntry(models.Model):
  xp_change = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  category = models.CharField(choices=XpLog.category_options, max_length=100)
  details = models.TextField()
  xp_log = models.ForeignKey(XpLog, editable=False)
  
class CharacterSheet(models.Model):
  name = models.CharField(max_length=100, default='New Sin-Eater')
  concept = models.CharField(max_length=400, blank=True)
  age = models.CharField(max_length=100, blank=True)
  dob = models.CharField(max_length=100, blank=True)
  virtue = models.IntegerField(choices=Game.virtue_options, blank=True, null=True)
  vice = models.IntegerField(choices=Game.vice_options, blank=True, null=True)
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
  
  def __unicode__(self):
    return u'%s' % (self.name)

  class Meta:
    abstract = True
    
class GeistCharacterSheet(CharacterSheet):
  faction = models.ForeignKey(Faction, blank=True, null=True)
  subrace = models.ForeignKey(Subrace, blank=True, null=True)
  
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
      
  def change_level(self):
    return ''

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from game_manager.models import Trait, Game, Geist, Faction, Subrace
    
class XpLog(models.Model):
  category_options = (('Game', 1), ('Attribute', 2), ('Merit', 3), ('Downtime', 4))

class XpEntry(models.Model):
  xp_change = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  category = models.CharField(choices=XpLog.category_options, max_length=100)
  details = models.TextField()
  xp_log = models.ForeignKey(XpLog)
  
class CharacterSheet(models.Model):
  name = models.CharField(max_length=100)
  concept = models.CharField(max_length=400)
  age = models.CharField(max_length=100)
  dob = models.CharField(max_length=100)
  virtue = models.IntegerField(choices=Game.virtue_options)
  vice = models.IntegerField(choices=Game.vice_options)
  xp_log = models.ForeignKey(XpLog) 
  user = models.ForeignKey(User)
  
  created_at = models.DateTimeField(default=datetime.now, editable=False)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
    
class GeistCharacterSheet(CharacterSheet):
  faction = models.ForeignKey(Faction)
  subrace = models.ForeignKey(Subrace)
  
class ChosenTrait(models.Model):
  trait = models.ForeignKey(Trait)
  level = models.IntegerField()
  character = models.ForeignKey(GeistCharacterSheet)
  specializations = models.CharField(max_length=300)
  created_at = models.DateTimeField(default=datetime.now, editable=False)
  updated_at = models.DateTimeField(auto_now=True)
  
  def change_level(self):
    return ''

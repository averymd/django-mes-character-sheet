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
    
  # def setup_merits(self):
    # self.merits = [
      # Trait(name = "Common Sense", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Danger Sense", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [2]),
      # Trait(name = "Eidetic Memory", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [2]),
      # Trait(name = "Encyclopedic Knowledge", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [4]),
      # Trait(name = "Holistic Awareness", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [3]),
      # Trait(name = "Language", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Meditative Mind", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Unseen Sense", trait_type = self.trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [3]),
      # Trait(name = "Ambidextrous", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      # Trait(name = "Brawling Dodge", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Direction Sense", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Disarm", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      # Trait(name = "Fast Reflexes", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1, 2]),
      # Trait(name = "Fighting Finesse", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      # Trait(name = "Fighting Style: Boxing", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Fighting Style: Kung Fu", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Fighting Style: Two Weapons", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Fleet of Foot", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false, specific_dots = [1, 2, 3]),
      # Trait(name = "Giant", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [4]),
      # Trait(name = "Gunslinger", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      # Trait(name = "Iron Stamina", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false, specific_dots = [1, 2, 3]),
      # Trait(name = "Iron Stomach", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      # Trait(name = "Natural Immunity", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Quick Draw", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Quick Healer", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [4]),
      # Trait(name = "Strong Back", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Strong Lungs", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      # Trait(name = "Stunt Driver", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      # Trait(name = "Toxin Resistance", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      # Trait(name = "Weaponry Dodge", trait_type = self.trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Allies", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Barfly", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = true, specific_dots = [1]),
      # Trait(name = "Contacts", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Fame", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false, specific_dots = [1, 2, 3]),
      # Trait(name = "Inspiring", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = true, specific_dots = [4]),
      # Trait(name = "Mentor", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Resources", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Retainer", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Status", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Striking Looks", trait_type = self.trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false, specific_dots = [2, 4])
    # ]
  
  # def setup_skills(self):  
    # this.Skills = [
      # Trait(name = "Academics", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Computer", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Crafts", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Investigation", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Medicine", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Occult", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Politics", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Science", trait_type = self.trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      # Trait(name = "Athletics", trait_type = self.trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Brawl", trait_type = self.trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Drive", trait_type = self.trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Firearms", trait_type = self.trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Larceny", trait_type = self.trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Stealth", trait_type = self.trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Weaponry", trait_type = self.trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      # Trait(name = "Animal Ken", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Empathy", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Expression", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Intimidation", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Persuasion", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "socialize", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Streetwise", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      # Trait(name = "Subterfuge", trait_type = self.trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false)
    # ]
            
  # def setup_trait_types(self):
    # self.trait_types = [ 
      # trait_type(name = "Attribute", default_xp_cost_per_dot = 5),
      # trait_type(name = "Skill", default_xp_cost_per_dot = 3),
      # trait_type(name = "Advantage", default_xp_cost_per_dot = 8),
      # trait_type(name = "Merit", default_xp_cost_per_dot = 2)
    # ]
    
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
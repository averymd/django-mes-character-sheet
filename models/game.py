from trait import Trait, trait_type

class Game:
  def __init__(self):
    self.name = ''
    self.subrace_name = ''
    self.subraces = []
    self.faction_name = ''
    self.factions = []
    self.energy_name = ''
    self.power_level_trait = Trait()
    self.morality = Trait()
    setup_trait_types();
    setup_attributes();
    setup_skills();
    setup_merits();
    self.willpower = Trait(name='Willpower', trait_type=self.trait_types[2]);
    self.powers = []
    self.vice_options = enum(envy=1, gluttony=2, greed=3, lust=4, pride=5, sloth=6, wrath=7)
    self.virtue_options = enum(charity=1, faith=2, fortitude=3, hope=4, justice=5, prudence=6, temperance=7)
  
  def setup_attributes(self):
    this.attributes = [
      Trait(name = "Intelligence", trait_type = self.trait_types[0], use = Trait.use_options.power, category = Trait.category_options.mental, uses_simple_calculation = False),
      Trait(name = "Wits", trait_type = trait_types[0], use = Trait.use_options.finesse, category = Trait.category_options.mental, uses_simple_calculation = False),
      Trait(name = "Resolve", trait_type = trait_types[0], use = Trait.use_options.resistance, category = Trait.category_options.mental, uses_simple_calculation = False),
      Trait(name = "Strength", trait_type = trait_types[0], use = Trait.use_options.power, category = Trait.category_options.physical, uses_simple_calculation = False),
      Trait(name = "Dexterity", trait_type = trait_types[0], use = Trait.use_options.finesse, category = Trait.category_options.physical, uses_simple_calculation = False),
      Trait(name = "Stamina", trait_type = trait_types[0], use = Trait.use_options.resistance, category = Trait.category_options.physical, uses_simple_calculation = False),
      Trait(name = "Presence", trait_type = trait_types[0], use = Trait.use_options.power, category = Trait.category_options.social, uses_simple_calculation = False),
      Trait(name = "Manipulation", trait_type = trait_types[0], use = Trait.use_options.finesse, category = Trait.category_options.social, uses_simple_calculation = False),
      Trait(name = "Composure", trait_type = trait_types[0], use = Trait.use_options.resistance, category = Trait.category_options.social, uses_simple_calculation = False)
    ]
  
  def setup_merits(self):
    self.merits = [
      Trait(name = "Common Sense", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Danger Sense", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [2]),
      Trait(name = "Eidetic Memory", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [2]),
      Trait(name = "Encyclopedic Knowledge", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [4]),
      Trait(name = "Holistic Awareness", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [3]),
      Trait(name = "Language", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Meditative Mind", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Unseen Sense", trait_type = trait_types[3], category = Trait.category_options.mental, uses_simple_calculation = true, specific_dots = [3]),
      Trait(name = "Ambidextrous", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      Trait(name = "Brawling Dodge", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Direction Sense", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Disarm", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      Trait(name = "Fast Reflexes", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1, 2]),
      Trait(name = "Fighting Finesse", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      Trait(name = "Fighting Style: Boxing", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Fighting Style: Kung Fu", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Fighting Style: Two Weapons", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Fleet of Foot", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false, specific_dots = [1, 2, 3]),
      Trait(name = "Giant", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [4]),
      Trait(name = "Gunslinger", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      Trait(name = "Iron Stamina", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = false, specific_dots = [1, 2, 3]),
      Trait(name = "Iron Stomach", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      Trait(name = "Natural Immunity", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Quick Draw", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Quick Healer", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [4]),
      Trait(name = "Strong Back", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Strong Lungs", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      Trait(name = "Stunt Driver", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [3]),
      Trait(name = "Toxin Resistance", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [2]),
      Trait(name = "Weaponry Dodge", trait_type = trait_types[3], category = Trait.category_options.physical, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Allies", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Barfly", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = true, specific_dots = [1]),
      Trait(name = "Contacts", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Fame", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false, specific_dots = [1, 2, 3]),
      Trait(name = "Inspiring", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = true, specific_dots = [4]),
      Trait(name = "Mentor", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Resources", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Retainer", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Status", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Striking Looks", trait_type = trait_types[3], category = Trait.category_options.social, uses_simple_calculation = false, specific_dots = [2, 4])
    ]
  
  def setup_skills(self):  
    this.Skills = [
      Trait(name = "Academics", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Computer", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Crafts", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Investigation", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Medicine", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Occult", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Politics", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Science", trait_type = trait_types[1], category = Trait.category_options.mental, uses_simple_calculation = false),
      Trait(name = "Athletics", trait_type = trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Brawl", trait_type = trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Drive", trait_type = trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Firearms", trait_type = trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Larceny", trait_type = trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Stealth", trait_type = trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Weaponry", trait_type = trait_types[1], category = Trait.category_options.physical, uses_simple_calculation = false),
      Trait(name = "Animal Ken", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Empathy", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Expression", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Intimidation", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Persuasion", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "socialize", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Streetwise", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false),
      Trait(name = "Subterfuge", trait_type = trait_types[1], category = Trait.category_options.social, uses_simple_calculation = false}
    ]
            
  def setup_trait_types(self):
    self.trait_types = [ 
      trait_type(name = "Attribute", default_xp_cost_per_dot = 5),
      trait_type(name = "Skill", default_xp_cost_per_dot = 3),
      trait_type(name = "Advantage", default_xp_cost_per_dot = 8),
      trait_type(name = "Merit", default_xp_cost_per_dot = 2)
    ]
    
class Subrace:
  def __init__():
    self.name = ''
    
class Faction:
  def __init__():
    self.name = ''
  
class Power:
  def __init__():
    self.name = ''
    self.xp_cost_per_dot = 0
    self.activation_traits = []
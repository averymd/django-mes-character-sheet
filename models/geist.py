from game import Game

class Geist(Game):
  def __init__(self):
    super().__init__()
    self.name = 'Geist'
    self.subrace_name = 'Threshold';
    self.faction_name = 'Archetype';
    self.energy_name = 'Psyche';
    self.morality = Trait(name = 'Synergy');
    self.trait_types.append(trait_type(name = 'Keys', default_xp_cost_per_dot = 10 ));
    setup_keys();
    setup_thresholds();
    setup_archetypes();
    
  def setup_archetypes(self):
    self.factions = [
      Faction(name = "Advocate"),
      Faction(name = "Bonepicker"),
      Faction(name = "Celebrant"),
      Faction(name = "Gatekeeper"),
      Faction(name = "Mourner"),
      Faction(name = "Necromancer"),
      Faction(name = "Pilgrim"),
      Faction(name = "Reaper")
    ]
    
  def setup_thresholds(self) {
    self.subraces = [
      Subrace(name = "Torn"),
      Subrace(name = "Silent"),
      Subrace(name = "Prey"),
      Subrace(name = "Stricken"),
      Subrace(name = "Forgotten")
    ]
    
  def setup_keys(self):
    self.keys = [
      Trait(name = "Cold Wind", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Grace-dirt", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Pyre Flame", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Tear-stained", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Industrial", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Passion", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Phantasmal", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Primeval", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Stigmata", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Stillness", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true),
      Trait(name = "Stygian", specific_dots = [1], trait_type = self.trait_types[4], uses_simple_calculation=true)
    ]
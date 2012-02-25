from charon_sheet.tools import enum

class TraitType:
  self.name = ''
  self.default_xp_cost_per_dot = ''

class Trait:
  def __init__(self):
    self.name = ''
    self.category = ''
    self.use = ''
    self.specific_dots = []
    self.trait_type = TraitType()
    self.custom_xp_per_dot = None
    self.category_options = enum(mental=1, physical=2, social=3)
    self.use_options = enum(power=1, finesse=2, resistance=3)
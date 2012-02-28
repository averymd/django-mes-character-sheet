from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from models import GeistCharacterSheet, ChosenTrait
from game_manager.models import Trait
from django.db.models import Count

class SheetCreation(TestCase):
  def setUp(self):
    self.user = User.objects.create_user('testuser', 'testuser@thecharonsheet.com', password='dummy')
  
  def test_posting_character_redirects_to_edit_version(self):
    """Case 308"""
    c = Client()
    c.login(username=self.user.username, password='dummy')
    response = c.post('/character-manager/character-sheet/', {'name':'Tasty SE'}, follow=True)
    self.assertRedirects(response, '/character-manager/character-sheet/1/')
    
  def test_saving_character_adds_attributes(self):
    """Case 309"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    self.assertEqual(len(sheet.chosentrait_set.filter(trait__trait_type__name='Attribute')), 9)
    
  def test_saving_character_adds_skills(self):
    """Case 310"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    self.assertEqual(len(sheet.chosentrait_set.filter(trait__trait_type__name='Skill')), 21)
    
class SheetEditing(TestCase):
  def setUp(self):
    self.user = User.objects.create_user('testuser', 'testuser@thecharonsheet.com', password='dummy')
    self.sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    self.c = Client()
    self.c.login(username=self.user.username, password='dummy')
    
  def test_attribute_fields_are_on_form(self):
    """Case 309"""
    response = self.c.get(self.sheet.get_absolute_url())
    self.assertContains(response, 'name="attribute-0-level"', count=1)
    self.assertContains(response, 'name="attribute-8-level"', count=1)
    
  def test_skill_fields_are_on_form(self):
    """Case 310"""
    response = self.c.get(self.sheet.get_absolute_url())
    self.assertContains(response, 'name="skill-0-level"', count=1)
    self.assertContains(response, 'name="skill-20-level"', count=1)
    
  def test_attribute_fields_are_filled(self):
    """Case 309"""
    response = self.c.get(self.sheet.get_absolute_url())
    self.assertContains(response, '<input type="text" name="attribute-0-level" value="1" id="id_attribute-0-level" />')
  
  def test_skill_fields_are_filled(self):
    """Case 310"""
    response = self.c.get(self.sheet.get_absolute_url())
    self.assertContains(response, '<input type="text" name="skill-0-level" value="0" id="id_skill-0-level" />')
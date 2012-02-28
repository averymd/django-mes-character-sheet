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
  fixtures = ['test_initial_data.json']
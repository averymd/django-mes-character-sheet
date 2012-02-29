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
    self.c = Client()
    self.c.login(username=self.user.username, password='dummy')
    self.post_data = {
      'name':u'Unhappy SE',
      'concept':u'Sad clown',
      'attribute-TOTAL_FORMS':u'2',
      'attribute-MAX_NUM_FORMS':u'',
      'attribute-INITIAL_FORMS':u'2',
      'attribute-0-level':u'2',
      'attribute-0-character':u'1',
      'attribute-0-id':u'1',
      'attribute-1-level':u'1',
      'attribute-1-character':u'1',
      'attribute-1-id':u'2',
      'skill-TOTAL_FORMS':u'2',
      'skill-MAX_NUM_FORMS':u'',
      'skill-INITIAL_FORMS':u'2',
      'skill-0-level':u'2',
      'skill-0-character':u'1',
      'skill-0-id':u'10',
      'skill-0-specializations':u'Research',
      'skill-1-level':u'1',
      'skill-1-character':u'1',
      'skill-1-id':u'11',
      'merit-TOTAL_FORMS':u'1',
      'merit-MAX_NUM_FORMS':u'',
      'merit-INITIAL_FORMS':u'1',
      'merit-0-level':u'2',
      'merit-0-character':u'1',
      'merit-0-trait':u'11',
      'merit-0-specializations':u'Sometimes',
      'merit-0-id':'',
    }
    
  def test_attribute_fields_are_on_form(self):
    """Case 309"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'name="attribute-0-level"', count=1)
    self.assertContains(response, 'name="attribute-8-level"', count=1)
    
  def test_skill_fields_are_on_form(self):
    """Case 310"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'name="skill-0-level"', count=1)
    self.assertContains(response, 'name="skill-20-level"', count=1)
    
  def test_merit_fields_are_on_form(self):
    """Case 311"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'name="merit-0-level"', count=1)
    self.assertContains(response, 'name="merit-2-level"', count=1)
    
  def test_attribute_fields_are_filled(self):
    """Case 309"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, '<input type="text" name="attribute-0-level" value="1" id="id_attribute-0-level" />')
  
  def test_skill_fields_are_filled(self):
    """Case 310"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, '<input type="text" name="skill-0-level" value="0" id="id_skill-0-level" />')
    
  def test_posting_edit_redirects_to_list(self):
    """Case 312"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.post(sheet.get_absolute_url(), self.post_data, follow=True)
    self.assertRedirects(response, '/character-manager/list/')
    
  def test_character_info_can_be_changed(self):
    """Case 312"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.post(sheet.get_absolute_url(), self.post_data, follow=True)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).concept, u'Sad clown')
    
  def test_attributes_can_be_changed(self):
    """Case 312"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.post(sheet.get_absolute_url(), self.post_data, follow=True)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.all().filter(trait__name='Intelligence')[0].level, 2)
    
  def test_skills_can_be_changed(self):
    """Case 312"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.post(sheet.get_absolute_url(), self.post_data, follow=True)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.all().filter(trait__name='Academics')[0].level, 1)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.all().filter(trait__name='Academics')[0].specializations, u'Research')
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.all().filter(trait__name='Investigations')[0].level, 1)
    
  def test_merits_can_be_added(self):
    """Case 312"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.post(sheet.get_absolute_url(), self.post_data, follow=True)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.all().filter(trait__name='Common Sense')[0].level, 2)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.all().filter(trait__name='Common Sense')[0].specializations, u'Sometimes')
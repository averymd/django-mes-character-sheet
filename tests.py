from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from datetime import datetime
from models import GeistCharacterSheet, ChosenTrait
from game_manager.models import Trait
from django.db.models import Count
import json

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
      'attribute-0-trait':u'%s' % (str(Trait.objects.get(name='Intelligence').id)),
      'attribute-1-level':u'1',
      'attribute-1-character':u'1',
      'attribute-1-id':u'2',
      'attribute-1-trait':u'%s' % (str(Trait.objects.get(name='Strength').id)),
      'skill-TOTAL_FORMS':u'2',
      'skill-MAX_NUM_FORMS':u'',
      'skill-INITIAL_FORMS':u'2',
      'skill-0-level':u'2',
      'skill-0-character':u'1',
      'skill-0-id':u'10',
      'skill-0-trait':u'%s' % (str(Trait.objects.get(name='Academics').id)),
      'skill-0-specializations':u'Research',
      'skill-1-level':u'1',
      'skill-1-character':u'1',
      'skill-1-id':u'11',
      'skill-1-trait':u'%s' % (str(Trait.objects.get(name='Investigation').id)),
      'merit-TOTAL_FORMS':u'1',
      'merit-MAX_NUM_FORMS':u'',
      'merit-INITIAL_FORMS':u'0',
      'merit-0-id':'',
      'merit-0-level':u'2',
      'merit-0-character':u'1',
      'merit-0-trait':u'%s' % (str(Trait.objects.get(name='Common Sense').id)),
      'merit-0-specializations':u'Sometimes',
      'xplog-TOTAL_FORMS':u'0',
      'xplog-MAX_NUM_FORMS':u'',
      'xplog-INITIAL_FORMS':u'0',
    }
    
  def test_attribute_fields_are_on_form(self):
    """Case 309"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'name="attribute-0-level"', count=5)
    self.assertContains(response, 'name="attribute-8-level"', count=5)
    
  def test_skill_fields_are_on_form(self):
    """Case 310"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'name="skill-0-level"', count=6)
    self.assertContains(response, 'name="skill-20-level"', count=6)
    
  def test_merit_fields_are_on_form(self):
    """Case 311"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'name="merit-0-level"', count=5)
    
  def test_xplog_fields_are_on_form(self):
    """Case 314"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'name="xplog-0-date"', count=1)
    
  def test_attribute_fields_are_filled(self):
    """Case 309"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.get(sheet.get_absolute_url())
    self.assertContains(response, 'id="id_attribute-0-level_0" value="1"')
   
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
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.get(trait__name='Intelligence').level, 2)
    
  def test_skills_can_be_changed(self):
    """Case 312"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.post(sheet.get_absolute_url(), self.post_data)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.get(trait__name='Academics').level, 2)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.get(trait__name='Academics').specializations, u'Research')
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.get(trait__name='Investigation').level, 1)
    
  def test_merits_can_be_added(self):
    """Case 312"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    response = self.c.post(sheet.get_absolute_url(), self.post_data, follow=True)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.get(trait__name='Common Sense').level, 2)
    self.assertEqual(GeistCharacterSheet.objects.get(pk=1).chosentrait_set.get(trait__name='Common Sense').specializations, u'Sometimes')
    
  def test_merit_dots_updated_when_single_dot_only_merit_selected(self):
    """Case 313"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    merit_selection = {
      'merit-id': u'11'
    }
    response = self.c.post('/character-manager/merit-dots/', merit_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    self.assertContains(response, '{"dots": [1]}')
    
  def test_merit_dots_updated_when_multi_dot_merit_selected(self):
    """Case 313"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    merit_selection = {
      'merit-id': u'26'
    }
    response = self.c.post('/character-manager/merit-dots/', merit_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    self.assertContains(response, '{"dots": [1, 2, 3, 4, 5]}')
  
  def test_merit_dot_update_fail_when_item_not_a_merit(self):
    """Case 313"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    # An attribute
    merit_selection = {
      'merit-id': u'5'
    }
    self.assertRaises(ValueError, self.c.post, '/character-manager/merit-dots/', merit_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    
  def test_merit_dot_update_fail_when_item_not_a_number(self):
    """Case 313"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    merit_selection = {
      'merit-id': u'deuce'
    }
    self.assertRaises(TypeError, self.c.post, '/character-manager/merit-dots/', merit_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    
class XpLogging(TestCase):
  def setUp(self):
    self.user = User.objects.create_user('testuser', 'testuser@thecharonsheet.com', password='dummy')
    self.c = Client()
    self.c.login(username=self.user.username, password='dummy')
    
  def test_xplog_total_spent_calculates_correctly(self):
    """Case 248"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    sheet.xp_log.xpentry_set.create(category=1, xp_change=10, date=datetime.now())
    sheet.xp_log.xpentry_set.create(category=1, xp_change=-4, date=datetime.now())
    sheet.xp_log.xpentry_set.create(category=1, xp_change=2, date=datetime.now())
    self.assertEqual(sheet.xp_spent(), 4)
    
  def test_xplog_total_earned_calculates_correctly(self):
    """Case 247"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    sheet.xp_log.xpentry_set.create(category=1, xp_change=10, date=datetime.now())
    sheet.xp_log.xpentry_set.create(category=1, xp_change=-4, date=datetime.now())
    sheet.xp_log.xpentry_set.create(category=1, xp_change=2, date=datetime.now())
    self.assertEqual(sheet.xp_earned(), 12)
    
  def test_xplog_total_remaining_calculates_correctly(self):
    """Case 246"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    sheet.xp_log.xpentry_set.create(category=1, xp_change=10, date=datetime.now())
    sheet.xp_log.xpentry_set.create(category=1, xp_change=-4, date=datetime.now())
    sheet.xp_log.xpentry_set.create(category=1, xp_change=2, date=datetime.now())
    self.assertEqual(sheet.xp_remaining(), 8)
    
  def test_xplog_xp_spent_for_cumulative_cost_purchase_calculates_correctly(self):
    """Case 316"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    trait_selection = {
      'trait-id': u'%s' % Trait.objects.get(name='Intelligence').id,
      'new-level': u'4', # Currently level 1
      'character-id': u'1'
    }
    response = self.c.post('/character-manager/trait-xp/', trait_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    json_resp = json.loads(response.content)
    self.assertEqual(json_resp['xpchange'], -45)
    
  def test_xplog_xp_spent_for_simple_cost_purchase_calculates_correctly(self):
    """Case 316"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    trait_selection = {
      'trait-id': u'%s' % Trait.objects.get(name='Striking Looks').id,
      'new-level': u'4', # Currently level 0
      'character-id': u'1'
    }
    response = self.c.post('/character-manager/trait-xp/', trait_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    json_resp = json.loads(response.content)
    self.assertEqual(json_resp['xpchange'], -8)
    
  def test_xplog_xp_spent_for_skill_purchase_calculates_correctly(self):
    """Case 316"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    trait_selection = {
      'trait-id': u'%s' % Trait.objects.get(name='Subterfuge').id,
      'new-level': u'4', # Currently level 0
      'character-id': u'1'
    }
    response = self.c.post('/character-manager/trait-xp/', trait_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    json_resp = json.loads(response.content)
    self.assertEqual(json_resp['xpchange'], -30)
    
  def test_xplog_xp_spent_for_single_dot_skill_purchase_calculates_correctly(self):
    """Case 316"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    trait_selection = {
      'trait-id': u'%s' % Trait.objects.get(name='Subterfuge').id,
      'new-level': u'1', # Currently level 0
      'character-id': u'1'
    }
    response = self.c.post('/character-manager/trait-xp/', trait_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    json_resp = json.loads(response.content)
    self.assertEqual(json_resp['xpchange'], -3)
    
  def test_xplog_xp_spent_for_cumulative_selloff_calculates_correctly(self):
    """Case 316"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    trait = sheet.chosentrait_set.get(trait=Trait.objects.get(name='Subterfuge'))
    trait.level = 3
    trait.save()
    trait_selection = {
      'trait-id': u'%s' % Trait.objects.get(name='Subterfuge').id,
      'new-level': u'1', # Currently level 3
      'character-id': u'1'
    }
    response = self.c.post('/character-manager/trait-xp/', trait_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    json_resp = json.loads(response.content)
    self.assertEqual(json_resp['xpchange'], 15)
    
  def test_xplog_xp_spent_for_simple_selloff_calculates_correctly(self):
    """Case 316"""
    sheet = GeistCharacterSheet.objects.create(name='Happy SE', user=self.user)
    sheet.chosentrait_set.create(trait=Trait.objects.get(name='Striking Looks'), level=4)
    trait_selection = {
      'trait-id': u'%s' % Trait.objects.get(name='Striking Looks').id,
      'new-level': u'2', # Currently level 4
      'character-id': u'1'
    }
    response = self.c.post('/character-manager/trait-xp/', trait_selection, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    json_resp = json.loads(response.content)
    self.assertEqual(json_resp['xpchange'], 4)
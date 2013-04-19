# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'XpLog'
        db.create_table('character_manager_xplog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('character_manager', ['XpLog'])

        # Adding model 'XpEntry'
        db.create_table('character_manager_xpentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('category', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('xp_change', self.gf('django.db.models.fields.IntegerField')()),
            ('details', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('xp_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_manager.XpLog'])),
        ))
        db.send_create_signal('character_manager', ['XpEntry'])

        # Adding model 'Character'
        db.create_table('character_manager_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='New Person', max_length=100)),
            ('concept', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('dob', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('virtue', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('vice', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mc_level_at_creation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('character_manager', ['Character'])

        # Adding model 'GeistCharacterSheet'
        db.create_table('character_manager_geistcharactersheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary_character', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('storyteller_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('storyteller_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('coordinator_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('coordinator_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('character', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_manager.Character'], unique=True)),
            ('xp_log', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_manager.XpLog'], unique=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game_manager.Faction'], null=True, blank=True)),
            ('subrace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game_manager.Subrace'], null=True, blank=True)),
        ))
        db.send_create_signal('character_manager', ['GeistCharacterSheet'])

        # Adding model 'ChosenTrait'
        db.create_table('character_manager_chosentrait', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trait', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game_manager.Trait'])),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_manager.GeistCharacterSheet'])),
            ('specializations', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('character_manager', ['ChosenTrait'])


    def backwards(self, orm):
        
        # Deleting model 'XpLog'
        db.delete_table('character_manager_xplog')

        # Deleting model 'XpEntry'
        db.delete_table('character_manager_xpentry')

        # Deleting model 'Character'
        db.delete_table('character_manager_character')

        # Deleting model 'GeistCharacterSheet'
        db.delete_table('character_manager_geistcharactersheet')

        # Deleting model 'ChosenTrait'
        db.delete_table('character_manager_chosentrait')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'character_manager.character': {
            'Meta': {'object_name': 'Character'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'concept': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'dob': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mc_level_at_creation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'New Person'", 'max_length': '100'}),
            'vice': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'virtue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'character_manager.chosentrait': {
            'Meta': {'object_name': 'ChosenTrait'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_manager.GeistCharacterSheet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'specializations': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'trait': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game_manager.Trait']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'character_manager.geistcharactersheet': {
            'Meta': {'object_name': 'GeistCharacterSheet'},
            'character': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_manager.Character']", 'unique': 'True'}),
            'coordinator_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'coordinator_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game_manager.Faction']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'primary_character': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'storyteller_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'storyteller_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'subrace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game_manager.Subrace']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'xp_log': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_manager.XpLog']", 'unique': 'True'})
        },
        'character_manager.xpentry': {
            'Meta': {'object_name': 'XpEntry'},
            'category': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'xp_change': ('django.db.models.fields.IntegerField', [], {}),
            'xp_log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_manager.XpLog']"})
        },
        'character_manager.xplog': {
            'Meta': {'object_name': 'XpLog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'game_manager.faction': {
            'Meta': {'object_name': 'Faction'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'factions'", 'to': "orm['game_manager.Geist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'game_manager.geist': {
            'Meta': {'object_name': 'Geist'},
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'attributes'", 'symmetrical': 'False', 'to': "orm['game_manager.Trait']"}),
            'energy_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'faction_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keys': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'keys'", 'symmetrical': 'False', 'to': "orm['game_manager.Trait']"}),
            'merits': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'merits'", 'symmetrical': 'False', 'to': "orm['game_manager.Trait']"}),
            'morality': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'morality'", 'to': "orm['game_manager.Trait']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'power_level_trait': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'power_level_trait'", 'to': "orm['game_manager.Trait']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'skills'", 'symmetrical': 'False', 'to': "orm['game_manager.Trait']"}),
            'subrace_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'willpower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'willpower'", 'to': "orm['game_manager.Trait']"})
        },
        'game_manager.subrace': {
            'Meta': {'object_name': 'Subrace'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subraces'", 'to': "orm['game_manager.Geist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'game_manager.trait': {
            'Meta': {'ordering': "['trait_type', 'category', 'use', 'name']", 'object_name': 'Trait'},
            'category': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'custom_xp_per_dot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'specific_dots': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'trait_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game_manager.TraitType']"}),
            'use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uses_simple_calculation': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'game_manager.traittype': {
            'Meta': {'object_name': 'TraitType'},
            'default_xp_cost_per_dot': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['character_manager']

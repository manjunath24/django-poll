# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'pollapp_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('poll_image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fingerprint', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pollapp', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'pollapp_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pollapp.Poll'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vote', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'pollapp', ['Choice'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'pollapp_poll')

        # Deleting model 'Choice'
        db.delete_table(u'pollapp_choice')


    models = {
        u'pollapp.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pollapp.Poll']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'pollapp.poll': {
            'Meta': {'object_name': 'Poll'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fingerprint': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poll_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['pollapp']
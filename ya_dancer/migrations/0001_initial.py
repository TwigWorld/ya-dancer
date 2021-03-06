# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HealthTable'
        db.create_table(u'ya_dancer_healthtable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('health_field', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ya_dancer', ['HealthTable'])


    def backwards(self, orm):
        # Deleting model 'HealthTable'
        db.delete_table(u'ya_dancer_healthtable')


    models = {
        u'ya_dancer.healthtable': {
            'Meta': {'object_name': 'HealthTable'},
            'health_field': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ya_dancer']
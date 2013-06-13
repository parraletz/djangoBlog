# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumnos'
        db.create_table(u'principal_alumnos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('edad', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'principal', ['Alumnos'])


    def backwards(self, orm):
        # Deleting model 'Alumnos'
        db.delete_table(u'principal_alumnos')


    models = {
        u'principal.alumnos': {
            'Meta': {'object_name': 'Alumnos'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'edad': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['principal']
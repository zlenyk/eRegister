# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'eRegisterUser'
        db.delete_table(u'users_eregisteruser')


    def backwards(self, orm):
        # Adding model 'eRegisterUser'
        db.create_table(u'users_eregisteruser', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'users', ['eRegisterUser'])


    models = {
        
    }

    complete_apps = ['users']
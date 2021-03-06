# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Classifier'
        db.create_table('packageindex_classifier', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('packageindex', ['Classifier'])

        # Adding model 'PackageIndex'
        db.create_table('packageindex_packageindex', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='pypi', unique=True, max_length=255)),
            ('xml_rpc_url', self.gf('django.db.models.fields.URLField')(default='http://pypi.python.org/pypi', max_length=200, blank=True)),
        ))
        db.send_create_signal('packageindex', ['PackageIndex'])

        # Adding model 'Package'
        db.create_table('packageindex_package', (
            ('index', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['packageindex.PackageIndex'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, primary_key=True)),
            ('auto_hide', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('packageindex', ['Package'])

        # Adding model 'Release'
        db.create_table('packageindex_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(related_name='releases', to=orm['packageindex.Package'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('metadata_version', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=64)),
            ('package_info', self.gf('packageindex.models.PackageInfoField')()),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('packageindex', ['Release'])

        # Adding unique constraint on 'Release', fields ['package', 'version']
        db.create_unique('packageindex_release', ['package_id', 'version'])

        # Adding model 'Distribution'
        db.create_table('packageindex_distribution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(related_name='distributions', to=orm['packageindex.Release'])),
            ('filename', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=255, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('md5_digest', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('filetype', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('pyversion', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('signature', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('mirrored_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('packageindex', ['Distribution'])

        # Adding unique constraint on 'Distribution', fields ['release', 'filetype', 'pyversion']
        db.create_unique('packageindex_distribution', ['release_id', 'filetype', 'pyversion'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Distribution', fields ['release', 'filetype', 'pyversion']
        db.delete_unique('packageindex_distribution', ['release_id', 'filetype', 'pyversion'])

        # Removing unique constraint on 'Release', fields ['package', 'version']
        db.delete_unique('packageindex_release', ['package_id', 'version'])

        # Deleting model 'Classifier'
        db.delete_table('packageindex_classifier')

        # Deleting model 'PackageIndex'
        db.delete_table('packageindex_packageindex')

        # Deleting model 'Package'
        db.delete_table('packageindex_package')

        # Deleting model 'Release'
        db.delete_table('packageindex_release')

        # Deleting model 'Distribution'
        db.delete_table('packageindex_distribution')


    models = {
        'packageindex.classifier': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Classifier'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'packageindex.distribution': {
            'Meta': {'unique_together': "(('release', 'filetype', 'pyversion'),)", 'object_name': 'Distribution'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5_digest': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'mirrored_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pyversion': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'distributions'", 'to': "orm['packageindex.Release']"}),
            'signature': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'packageindex.package': {
            'Meta': {'ordering': "['name']", 'object_name': 'Package'},
            'auto_hide': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'index': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['packageindex.PackageIndex']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'})
        },
        'packageindex.packageindex': {
            'Meta': {'object_name': 'PackageIndex'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "'pypi'", 'unique': 'True', 'max_length': '255'}),
            'xml_rpc_url': ('django.db.models.fields.URLField', [], {'default': "'http://pypi.python.org/pypi'", 'max_length': '200', 'blank': 'True'})
        },
        'packageindex.release': {
            'Meta': {'ordering': "['-created']", 'unique_together': "(('package', 'version'),)", 'object_name': 'Release'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata_version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '64'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'releases'", 'to': "orm['packageindex.Package']"}),
            'package_info': ('packageindex.models.PackageInfoField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['packageindex']

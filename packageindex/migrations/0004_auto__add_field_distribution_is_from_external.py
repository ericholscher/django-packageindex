# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Distribution.is_from_external'
        db.add_column('packageindex_distribution', 'is_from_external', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Distribution.is_from_external'
        db.delete_column('packageindex_distribution', 'is_from_external')


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
            'is_from_external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'updated_from_remote_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'packageindex.packageindex': {
            'Meta': {'object_name': 'PackageIndex'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'simple_url': ('django.db.models.fields.URLField', [], {'default': "'http://pypi.python.org/simple'", 'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "'pypi'", 'unique': 'True', 'max_length': '255'}),
            'updated_from_remote_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'xml_rpc_url': ('django.db.models.fields.URLField', [], {'default': "'http://pypi.python.org/pypi'", 'max_length': '200', 'blank': 'True'})
        },
        'packageindex.release': {
            'Meta': {'ordering': "['-created']", 'unique_together': "(('package', 'version'),)", 'object_name': 'Release'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_from_external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'metadata_version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '64'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'releases'", 'to': "orm['packageindex.Package']"}),
            'package_info': ('packageindex.models.PackageInfoField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['packageindex']

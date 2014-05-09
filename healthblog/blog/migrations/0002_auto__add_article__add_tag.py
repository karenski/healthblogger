# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('blurb', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'blog', ['Article'])

        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('topic_tag', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'blog', ['Tag'])

        # Adding M2M table for field articles on 'Tag'
        m2m_table_name = db.shorten_name(u'blog_tag_articles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False)),
            ('article', models.ForeignKey(orm[u'blog.article'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'article_id'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'blog_article')

        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')

        # Removing M2M table for field articles on 'Tag'
        db.delete_table(db.shorten_name(u'blog_tag_articles'))


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'blurb': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Article']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'topic_tag': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['blog']
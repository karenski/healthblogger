from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField()
	blurb = models.TextField(max_length=500)
	image = models.URLField(default="")
	views = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Tag(models.Model):
	articles = models.ManyToManyField(Article)
	name = models.CharField(max_length=128, unique=True)
	topic_tag = models.BooleanField(default=False)
	article_count = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name



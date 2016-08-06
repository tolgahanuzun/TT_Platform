from __future__ import unicode_literals

from django.db import models

class Populer(models.Model):
	twitter_name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return "%s" % (self.twitter_name)
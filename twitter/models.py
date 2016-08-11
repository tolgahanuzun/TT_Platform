from __future__ import unicode_literals

from django.db import models

class Populer(models.Model):
	twitter_name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return "%s" % (self.twitter_name)


class Kac_Kullanici(models.Model):
	insan_limiti = models.IntegerField(default=10)

	def __unicode__(self):
		return "%s" % ("limit")

class Rt_Kullanicimodel(models.Model):
	rt_name = models.IntegerField()
	
	def __unicode__(self):
		return "%s" % (self.rt_name)

class Rt_Kacmodel(models.Model):
	rt_limiti = models.IntegerField(default=11)


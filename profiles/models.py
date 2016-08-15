from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User)
	
	consumer_keys = models.CharField(max_length=120,null=True ,blank=True)
	consumer_secrets = models.CharField(max_length=120,null=True ,blank=True)
	access_tokens = models.CharField(max_length=120,null=True ,blank=True)
	access_token_secrets = models.CharField(max_length=120,null=True ,blank=True)


	def __unicode__(self):
		return "%s" % (self.user)

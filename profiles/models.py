from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User)
	
	tumblr_consumer_keys = models.CharField(max_length=120,null=True ,blank=True)
	tumblr_consumer_secrets = models.CharField(max_length=120,null=True ,blank=True)
	tumblr_access_tokens = models.CharField(max_length=120,null=True ,blank=True)
	tumblr_access_token_secrets = models.CharField(max_length=120,null=True ,blank=True)
	twitter_consumer_keys = models.CharField(max_length=120,null=True ,blank=True)
	twitter_consumer_secrets = models.CharField(max_length=120,null=True ,blank=True)
	twitter_access_tokens = models.CharField(max_length=120,null=True ,blank=True)
	twitter_access_token_secrets = models.CharField(max_length=120,null=True ,blank=True)


	def __unicode__(self):
		return "%s" % (self.user)

from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

class Like_Limit(models.Model):
	like = models.IntegerField(default=1,validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ])

	def __unicode__(self):
		return "%s" % (self.like)

class Img_Post(models.Model):
	urllink = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s" % (self.urllink)

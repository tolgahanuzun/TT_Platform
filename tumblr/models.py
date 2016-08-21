#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

class Like_Limit(models.Model):
	like = models.IntegerField(default=1,validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

	def __unicode__(self):
		return "%s" % (self.like)

class Img_Post(models.Model):
	urllink = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s" % (self.urllink)

class Img_Content(models.Model):
	blogname = models.CharField(max_length=100,)
	context = models.TextField()
	tag = models.CharField(max_length=500,)

	def __unicode__(self):
		return "%s" % (self.blogname)

class Rt_Put(models.Model):
	rtlink = models.CharField(max_length=250)

	def __unicode__(self):
		return "%s" % (self.rtlink)

class Rt_Push(models.Model):
	blogname = models.CharField(max_length=100,)
	context = models.TextField()

	def __unicode__(self):
		return "%s" % (self.blogname)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GpioModel(models.Model):
	pin = models.IntegerField()
	stav = models.BooleanField()
	cas = models.DateTimeField(blank=True, null=True)
	poznamka = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.pin 
		
class Plan(models.Model):
	jmeno = models.CharField(max_length=50)
	pin = models.ForeignKey(GpioModel)
	casZacatek = models.DateTimeField()
	casKonec = models.DateTimeField()
	poznamka = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.jmeno 
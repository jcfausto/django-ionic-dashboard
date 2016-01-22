from __future__ import unicode_literals

from django.db import models

class Organization(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100, blank=False)
	owner = models.ForeignKey('auth.User', related_name='organizations')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('created',)

class Team(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100, blank=False)
	owner = models.ForeignKey('Organization', related_name='teams')

	class Meta:
		ordering = ('created',)
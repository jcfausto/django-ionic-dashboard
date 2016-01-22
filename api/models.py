from __future__ import unicode_literals

from django.db import models

class Organization(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100, blank=False)

	class Meta:
		ordering = ('created',)
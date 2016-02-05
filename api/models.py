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

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('created',)

class Kpi(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('Team', related_name='kpis')
	name = models.CharField(max_length=20, blank=False)
	lower_limit = models.FloatField(default=0.0, blank=False)
	upper_limit = models.FloatField(default=0.0, blank=False)
	better_when = models.CharField(max_length=5, blank=False, default='upper')


	def __str__(self):
		return '%d: %s' % (self.id, self.name)

	class Meta:
		ordering = ('created',)


class KpiValue(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('Kpi', related_name='values')
	value = models.FloatField(default=0.0, blank=False)

	@property
	def status(self):
		result = 'yellow'

		if self.owner.better_when.lower() == 'upper':
			if self.value > self.owner.upper_limit:
				result = 'green'
			elif self.value < self.owner.lower_limit:
				result = 'red'

		if self.owner.better_when.lower() == 'lower':
			if self.value < self.owner.lower_limit:
				result = 'green'
			elif self.value > self.owner.upper_limit:
				result = 'red'

		return result	

	def __str__(self):
		return self.value

	class Meta:
		ordering = ('created',)

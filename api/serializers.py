from rest_framework import serializers
from api.models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organization
		fields = ('id', 'name',)
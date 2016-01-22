from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Organization, Team

class UserSerializer(serializers.ModelSerializer):
	#need to be initialized in order to be listed in the metaclass fields
	organizations = serializers.PrimaryKeyRelatedField(many=True, queryset=Organization.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'organizations')

class OrganizationSerializer(serializers.ModelSerializer):	
	#need to be initialized in order to be listed in the metaclass fields	
	owner = serializers.ReadOnlyField(source='owner.username')
	teams = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

	class Meta:
		model = Organization
		fields = ('id', 'name', 'owner', 'teams')

class TeamSerializer(serializers.ModelSerializer):
	#need to be initialized in order to be listed in the metaclass fields	
	owner = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())

	class Meta:
		model = Team
		fields = ('id', 'name', 'owner')
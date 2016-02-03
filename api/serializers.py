from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Organization, Team, Kpi, KpiValue, KpiLimit

class UserSerializer(serializers.ModelSerializer):
	#need to be initialized in order to be listed in the metaclass fields
	organizations = serializers.PrimaryKeyRelatedField(many=True, queryset=Organization.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'organizations')


class KpiValueSerializer(serializers.ModelSerializer):
	#need to be initialized in order to be listed in the metaclass fields	
	owner = serializers.PrimaryKeyRelatedField(queryset=Kpi.objects.all())

	class Meta:
		model = KpiValue
		fields = ('id', 'value', 'owner')


class KpiLimitSerializer(serializers.ModelSerializer):
	#need to be initialized in order to be listed in the metaclass fields	
	owner = serializers.PrimaryKeyRelatedField(queryset=Kpi.objects.all())

	class Meta:
		model = KpiLimit
		fields = ('id', 'lower_limit', 'upper_limit', 'owner')


class KpiSerializer(serializers.ModelSerializer):
	owner = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
	values = KpiValueSerializer(many=True, read_only=True)
	limits = KpiLimitSerializer(many=True, read_only=True)

	class Meta:
		model = Kpi
		fields = ('id', 'name', 'values', 'limits', 'owner')


class TeamSerializer(serializers.ModelSerializer):
	#need to be initialized in order to be listed in the metaclass fields	
	owner = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
	kpis = KpiSerializer(many=True, read_only=True)

	class Meta:
		model = Team
		fields = ('id', 'name', 'kpis', 'owner')

class OrganizationSerializer(serializers.ModelSerializer):	
	#need to be initialized in order to be listed in the metaclass fields	
	owner = serializers.ReadOnlyField(source='owner.username')
	teams = TeamSerializer(many=True, read_only=True)
	#teams = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

	class Meta:
		model = Organization
		fields = ('id', 'name', 'owner', 'teams')

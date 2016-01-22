from django.shortcuts import render
from .mixins import JSONResponseMixin
from rest_framework.views import APIView
from api.models import Organization
from api.serializers import OrganizationSerializer

class PingView(APIView):

	def get(self, request):
		"""
		Just responds with Pong
		"""
		data = {'ping': 'pong'}

		return JSONResponseMixin(data)


class OrganizationView(APIView):

	def get(self, request):
		"""
		List all organizations registered in the system
		"""
		organizations = Organization.objects.all()
		serialized_data = OrganizationSerializer(organizations, many=True)
		return JSONResponseMixin(serialized_data.data)
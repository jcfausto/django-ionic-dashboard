from rest_framework import generics
from rest_framework.views import APIView
from .mixins import JSONResponseMixin
from api.models import Organization
from api.serializers import OrganizationSerializer

class PingView(APIView):

	def get(self, request):
		"""
		Just responds with Pong
		"""
		data = {'ping': 'pong'}

		return JSONResponseMixin(data)

class OrganizationList(generics.ListCreateAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer	

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer	
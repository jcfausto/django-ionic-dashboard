from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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

class OrganizationDetailView(APIView):

	def get(self, request, pk):
		"""
		Return details for a given Organization
		"""
		try:
			organization = Organization.objects.get(pk=pk)
		except Organization.DoesNotExist:
			return HttpResponse(status=404)

		serialized_data = OrganizationSerializer(organization)
		return JSONResponseMixin(serialized_data.data)
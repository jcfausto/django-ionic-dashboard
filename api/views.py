from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .mixins import JSONResponseMixin
from api.models import Organization, Team
from api.serializers import UserSerializer, OrganizationSerializer, TeamSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'organizations': reverse('organization-list', request=request, format=format),
        'teams': reverse('teams-list', request=request, format=format),
    })

class PingView(APIView):

	def get(self, request):
		"""
		Just responds with Pong
		"""
		data = {'ping': 'pong'}

		return JSONResponseMixin(data)

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class OrganizationList(generics.ListCreateAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer	

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)	

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer

class TeamList(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer	
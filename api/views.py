from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions

from .mixins import JSONResponseMixin
from api.models import Organization, Team, Kpi, KpiValue
from api.serializers import (
	UserSerializer, OrganizationSerializer, 
	TeamSerializer, KpiSerializer, KpiValueSerializer,
)

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'organizations': reverse('organization-list', request=request, format=format),
		'teams': reverse('team-list', request=request, format=format),
    })

class PingView(APIView):

	def get(self, request):
		"""
		Just responds with Pong
		"""
		data = {'ping': 'pong'}

		return JSONResponseMixin(data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)		

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)	


#TODO: The views below could be transformed into viewsets later

class KpiList(generics.ListCreateAPIView):
	queryset = Kpi.objects.all()
	serializer_class = KpiSerializer

class KpiDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Kpi.objects.all()
	serializer_class = KpiSerializer

class KpiValueList(generics.ListCreateAPIView):
	queryset = KpiValue.objects.all()
	serializer_class = KpiValueSerializer

class KpiValueDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = KpiValue.objects.all()
	serializer_class = KpiValueSerializer
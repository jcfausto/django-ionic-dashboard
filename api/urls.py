from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, url, include
from api.views import PingView, UserList, UserDetail, TeamList, TeamDetail, OrganizationList, OrganizationDetail

router = DefaultRouter()

urlpatterns = patterns('',
	url(r'ping/$', PingView.as_view(), name='ping'),
	url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'users/$', UserList.as_view(), name='user-list'),
	url(r'users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
	url(r'organizations/$', OrganizationList.as_view(), name='organization-list'),
	url(r'organizations/(?P<pk>[0-9]+)/$', OrganizationDetail.as_view(), name='organization-detail'),
	url(r'teams/$', TeamList.as_view(), name='team-list'),
	url(r'teams/(?P<pk>[0-9]+)/$', TeamDetail.as_view(), name='team-detail'),
)
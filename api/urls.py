from django.conf.urls import patterns, url
from api.views import PingView, OrganizationView, OrganizationDetailView

urlpatterns = patterns('',
	url(r'ping/$', PingView.as_view(), name='ping'),
	url(r'organizations/$', OrganizationView.as_view(), name='organizations'),
	url(r'organizations/(?P<pk>[0-9]+)/$', OrganizationDetailView.as_view(), name='organization details'),
)
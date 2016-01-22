from django.conf.urls import patterns, url, include
from api.views import PingView, OrganizationList, OrganizationDetail

urlpatterns = patterns('',
	url(r'ping/$', PingView.as_view(), name='ping'),
	url(r'organizations/$', OrganizationList.as_view(), name='organizations'),
	url(r'organizations/(?P<pk>[0-9]+)/$', OrganizationDetail.as_view(), name='organization details'),
)
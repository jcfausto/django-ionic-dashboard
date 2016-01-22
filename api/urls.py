from django.conf.urls import patterns, url
from api.views import PingView, OrganizationView

urlpatterns = patterns('',
	url(r'/ping/', PingView.as_view(), name='ping'),
	url(r'/organizations/', OrganizationView.as_view(), name='organizations')
)
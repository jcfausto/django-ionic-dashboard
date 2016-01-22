from django.conf.urls import patterns, url
from api.views import PingView

urlpatterns = patterns('',
	url(r'/ping/', PingView.as_view(), name='ping'),
)
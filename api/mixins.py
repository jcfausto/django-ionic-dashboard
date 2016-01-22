from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

class JSONResponseMixin(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponseMixin, self).__init__(content, **kwargs)
from django.shortcuts import render
from .mixins import JSONResponseMixin
from rest_framework.views import APIView

class PingView(APIView):

	def get(self, request):
		"""
		Just responds with Pong
		"""
		data = {'ping': 'pong'}

		return JSONResponseMixin(data)
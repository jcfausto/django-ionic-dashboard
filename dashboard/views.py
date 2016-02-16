from django.shortcuts import render

def index (request):
	return render(request, 'static/index.html', None)
from django.shortcuts import render

def index(request):
	context = {
		'sitelogo' : 'bear_landing'
	}

	return render(
		request,
		'index.html',
		context
	)# Create your views here.

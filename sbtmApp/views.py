from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def startEngine(request):
	return render(request, 'startEngine.html', {})


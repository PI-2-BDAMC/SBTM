from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def startEngine(request):
	return render(request, 'startEngine.html', {})


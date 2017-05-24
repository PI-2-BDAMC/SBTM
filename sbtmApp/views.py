from django.shortcuts import render_to_response, render

def index(request):
    return render(request, 'index.html', {})

def startEngine(request):
    return render(request, 'startEngine.html', {})

def previousTests(request):
    return render(request, 'previousTests.html', {})

def graphs(request):
    return render(request, 'graphs.html', {})
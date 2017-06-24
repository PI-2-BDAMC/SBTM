from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
import socket
from .graphs import ChartData
import json

def index(request):
    return render(request, 'index.html', {})

def startEngine(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/signin/?next=%s' % request.path)
    else:
        return render(request, 'startEngine.html', {})

def previousTests(request):
    return render(request, 'previousTests.html', {})

def graphs(request):
	#sendMessage()
	return render(request, 'graphs.html', {})

def sendMessage():
	TCP_IP = "192.168.0.21"
	TCP_PORT = 5005
	BUFFER_SIZE = 1024
	MESSAGE = "Hello, World!"

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((TCP_IP, TCP_PORT))
	sock.send(MESSAGE)
	data = sock.recv(BUFFER_SIZE)
	sock.close()

def chart_data_json(request):
    data = {}
    data['chart_data'] = ChartData.get_temperature_sensor_data(request.user)

    return HttpResponse(json.dumps(data), content_type='application/json')
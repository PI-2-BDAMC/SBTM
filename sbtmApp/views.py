from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
import socket
from .graphs import ChartData
from .recorder import Recorder
from .models import BenchTest
import json

def index(request):
    return render(request, 'index.html', {})

def startEngine(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/signin/?next=%s' % request.path)
    else:
        return render(request, 'startEngine.html', {})

def previousTests(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/signin/?next=%s' % request.path)
    else:
        ensaios = BenchTest.objects.filter(userBenchTest = request.user)

        return render(request, 'previousTests.html', {'ensaios':ensaios})

def graphs(request):
	#sendMessage()
	#test = BenchTest(userBenchTest=request.user)
	#test.save()
  return render(request, 'graphs.html', {})

def sendMessage():

  TCP_IP = '192.168.0.100'
  TCP_PORT = 5005
  BUFFER_SIZE = 2
  MESSAGE = "on"
 
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((TCP_IP, TCP_PORT))
  s.send(MESSAGE)
  data = s.recv(BUFFER_SIZE)
  s.close()
  
  print "received data:", data

def chart_data_json(request):
    data = []
    params = request.GET
    name = params.get('name', '')

    if name == 'tmp_sensor':
      data = ChartData.get_temperature_sensor_data(request.user)

    elif name == 'rpm_sensor':
      data = ChartData.get_rpm_sensor_data(request.user)

    elif name == 'fuel_comsumption':
      data = ChartData.get_fuel_comsumption(request.user)

    elif name == 'admission_temperature':
      data = ChartData.get_admission_temperature(request.user)

    return HttpResponse(json.dumps(data), content_type='application/json')

def data_from_sensors(request):

    if request.method == "GET":
      rd = Recorder()
      rd.aquisition(request.user)

    return HttpResponse(json.dumps(" "), content_type='application/json')

def reports(request):
    
    data = []
    params = request.GET
    identifier = params.get('id', '')
    descricao = params.get('descricao', '')
    dateBenchTest = params.get('dateBenchTest', '')

    return render(request, 'reports.html', {'identifier':identifier, 'descricao':descricao, 'dateBenchTest':dateBenchTest})
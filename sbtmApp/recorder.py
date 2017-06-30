from .models import BenchTest
import socket

class Recorder(object):

	def aquisition(self, user):

	    UDP_IP_SERVER = "192.168.0.31"
	    UDP_IP = "192.168.0.39"
	    UDP_PORT = 5005
	    
	    sock = socket.socket(socket.AF_INET, # Internet
	                         socket.SOCK_DGRAM) # UDP

	    sock.bind((UDP_IP_SERVER, UDP_PORT))

	    while True:
	        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	        print addr
	        self.createSensorObjects(data, user)

	def createSensorObjects(self, data_from_rasp, user):

		benchtests = BenchTest.objects.filter(userBenchTest = user)
		benchtest = benchtests.last()
		sensor_id = int(data_from_rasp[0])

		if  sensor_id in range(0, 5):
			value = data_from_rasp.strip(str(sensor_id)).strip(".").strip(" ")
			print(value + "#######################################")
			#benchtest.pressuresensor_set.create(valuePressure=value, localSensor=sensor_id)

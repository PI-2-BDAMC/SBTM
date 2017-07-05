from .models import BenchTest
from datetime import datetime, timedelta

class ChartData(object):

    @classmethod
    def get_temperature_sensor_data(cls, user):
    	benchtests = BenchTest.objects.filter(userBenchTest = user)
    	sensor_temperature = benchtests.last().temperaturesensor_set.last()

        data = sensor_temperature.valueTemperature

        return data

    @classmethod
    def get_admission_temperature(cls, user):
        data = []
        benchtests = BenchTest.objects.filter(userBenchTest = user)
        sensor_0_temperature = benchtests.last().temperaturesensor_set.filter(localSensor=0).last().valueTemperature
        sensor_1_temperature = benchtests.last().temperaturesensor_set.filter(localSensor=1).last().valueTemperature

        data = [sensor_0_temperature, sensor_1_temperature]

        return data

    @classmethod
    def get_rpm_sensor_data(cls, user):
    	benchtests = BenchTest.objects.filter(userBenchTest = user)
    	rpm_data = benchtests.last().rpmsensor_set.last()

        data = rpm_data.valueRPM

        return data

    @classmethod
    def get_fuel_comsumption(cls, user):
    	benchtests = BenchTest.objects.filter(userBenchTest = user)
    
    	now = datetime.now()
    	earlier = now - timedelta(seconds=30)

    	cell_data_1 = benchtests.last().loadcell_set.filter(date__range =(earlier,now)).first().valueCharge

    	cell_data_2 = benchtests.last().loadcell_set.last().valueCharge

    	fuel_comsumption = (cell_data_1 - cell_data_2)/0.75

    	data = fuel_comsumption

    	return data
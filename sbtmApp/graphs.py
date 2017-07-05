from .models import BenchTest
from datetime import datetime, timedelta
from math import sqrt

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

    	return round(data, 2)

    @classmethod
    def get_air_comsumption(cls, user):
        benchtests = BenchTest.objects.filter(userBenchTest = user)
        
        admission_temperature = benchtests.last().temperaturesensor_set.last().valueTemperature
        admission_pressure1 = benchtests.last().pressuresensor_set.filter(localSensor=2).last().valuePressure
        admission_pressure2 = benchtests.last().pressuresensor_set.filter(localSensor=3).last().valuePressure

        pCaixa = (admission_pressure1*10000)/101.308
        pAtm = (admission_pressure2*10000)/101.308

        pAtm2 = admission_pressure2/101.308

        dh = pAtm - pCaixa

        pB = pAtm2

        tbb = admission_temperature


        car = 121.06*sqrt((dh*pB)/(10*(tbb+273)))


        return round(car, 2)

    @classmethod
    def get_pressure_sensor_0_data(cls, user, test_id):
        benchtests = BenchTest.objects.filter(userBenchTest = user)
        benchtest = benchtests.get(id=test_id)
        sensor_temperatures = benchtest.pressuresensor_set.filter(localSensor = 6).all()

        data = {'times': [], 'values': []}
        for temp in sensor_temperatures:
            data['times'].append(temp.date.strftime('%X'))
            data['values'].append(temp.valuePressure)

        return data

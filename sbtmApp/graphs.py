from .models import BenchTest

class ChartData(object):

    @classmethod
    def get_temperature_sensor_data(cls, user):
    	benchtests = BenchTest.objects.filter(userBenchTest = user)
    	sensor_temperature = benchtests.last().temperaturesensor_set.last()

        data = sensor_temperature.valueTemperature

        return data

    @classmethod
    def get_rpm_sensor_data(cls, user):
    	benchtests = BenchTest.objects.filter(userBenchTest = user)
    	rpm_data = benchtests.last().rpmsensor_set.last()

        data = rpm_data.valueRPM

        return data
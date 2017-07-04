from .models import BenchTest

class ChartData(object):

    @classmethod
    def get_temperature_sensor_data(cls, user):
    	benchtests = BenchTest.objects.filter(userBenchTest = user)
    	sensor_temperature = benchtests.last().temperaturesensor_set.last()

        data = sensor_temperature.valueTemperature

        return data
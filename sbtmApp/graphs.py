from .models import BenchTest

class ChartData(object):

    @classmethod
    def get_temperature_sensor_data(cls, user):
    	benchtests = BenchTest.objects.filter(userBenchTest = user)
    	sensor_temperatures = benchtests.last().temperaturesensor_set.all()

        data = {'times': [], 'values': []}
        for dt in sensor_temperatures:
            data['times'].append(dt.date.strftime('%X'))
            data['values'].append(dt.valueTemperature)

        return data
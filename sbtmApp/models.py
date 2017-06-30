from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here..


class BenchTest(models.Model):
	"""docstring for BenchTest"""
	
	userBenchTest =  models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, db_tablespace="indexes")
	dateBenchTest = models.DateTimeField(auto_now_add=True,blank=False)
	descricao = models.CharField(max_length=200, db_index=True, db_tablespace="indexes")


class TemperatureSensor(models.Model):
	"""docstring for Temperature"""

	benchTest = models.ForeignKey(BenchTest, on_delete=models.CASCADE, db_index=True, db_tablespace="indexes")
	valueTemperature = models.FloatField(db_index=True, db_tablespace="indexes")
	date = models.DateTimeField(default=datetime.now, blank=False, db_index=True, db_tablespace="indexes")
	localSensor = models.IntegerField(default=0, blank=False, db_index=True, db_tablespace="indexes")

	def __str__(self):
		return str(round(self.valueTemperature, 2))

class PressureSensor(models.Model):
	"""docstring for Pression"""

	benchTest = models.ForeignKey(BenchTest, on_delete=models.CASCADE, db_index=True, db_tablespace="indexes")
	valuePressure = models.FloatField(blank=False, db_index=True, db_tablespace="indexes")
	date = models.DateTimeField(default=datetime.now, blank=False, db_index=True, db_tablespace="indexes")
	localSensor = models.IntegerField(default=0, blank=False, db_index=True, db_tablespace="indexes")

class RpmSensor(models.Model):
	"""docstring for ClassName"""

	benchTest = models.ForeignKey(BenchTest, on_delete=models.CASCADE, db_index=True, db_tablespace="indexes")
	valueRPM = models.FloatField(blank=False, db_index=True, db_tablespace="indexes")
	date = models.DateTimeField(default=datetime.now, blank=False, db_index=True, db_tablespace="indexes")
	
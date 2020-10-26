from django.db import models

# Create your models here.null=True, blank=True

class Users(models.Model):
	employee_id = models.CharField(max_length=10, unique=True)  #HQ001
	name = models.CharField(max_length=100) #Joel Crawford
	age = models.IntegerField() #27
	ranking = models.FloatField() #3.5

	#upload photo function
	def upload_photo(self, filename):
		path = 'hrm/photo/{}'.format(filename)
		return path

	photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)


	#upload   file function
	def upload_file(self, filename):
		path = 'hrm/file/{}'.format(filename)
		return path

	resume = models.ImageField(upload_to=upload_file, null=True, blank=True)


	#showing model name instead of user
	def __str__(self):
		return f"{self.employee_id} - {self.name}"

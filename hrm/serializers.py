#importing serializers
from rest_framework import serializers

#importing models ie Users
from hrm.models import Users

class UsersSerializer(serializers.ModelSerializer):   #inherit serializers.ModelSerializer becuase we want to serialize a model
	#create a Meta Class
	class Meta:
		model = Users #use user model
		# fields = ('name','employee_id')
		# name = serializers.CharField(required=False) #setting name not as required, controlling at serializer level or model level
		employee_id = serializers.CharField(required=False)
		name = serializers.CharField(required=False)
		ranking = serializers.FloatField(required=False)
		fields = '__all__' #use all fields, incase we wanted name and employee_id we use ('name','employee_id')

 
#This is the file linked to our urls
#so it can be accessed through url
#so exuting sending a url to django, this file is executed


#We need to import 2 things, the api view and response
#APIVIEW looks for few functions of  GET, PUT, POST and DELETE


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hrm.models import Users
from .serializers import *


class UserList(APIView):
	def get(self, request):
		#we need to specify what we want to display, ie we will display all the emplyees
		#get the model to be passed in the serialzer

		model = Users.objects.all() #what do we need to display, display emplyee inside the hrm, hence we import serialize

		serializer = UsersSerializer(model, many=True) #many=True means return all the items
		return Response(serializer.data) #serializer from  serializer = UsersSerializers(model, many=True)

	def post(self, request):
		#we need a serializer when creating a post object
		serializer = UsersSerializer(data=request.data)  # we provide our data
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



	##Different urls, we need to create diff class
class UserDetail(APIView):
	def get(self, request, employee_id):
		#Besides reques we also need emplooye id, we need employee_id in get and put
		#get the model to be passed in the serialzer

		# model = Users.objects.all() #what do we need to display, display emplyee inside the hrm, hence we import serialize
		try:
			model = Users.objects.get(id=employee_id) # we get if id is equal to employee_id
		except Users.DoesNotExist:
			return Response(f'User with {employee_id} is Not Found in the database', status=status.HTTP_404_NOT_FOUND)

		serializer = UsersSerializer(model) #many=True, serilaizers you are providing an array or list, hence this only works for get all request, BUT for GET only a single request its not so
		return Response(serializer.data) #serializer from  serializer = UsersSerializers(model, many=True)


	def put(self, request, employee_id):
		try:
			model = Users.objects.get(id=employee_id) # we get if id is equal to employee_id
		except Users.DoesNotExist:
			return Response(f'User with {employee_id} is Not Found in the database', status=status.HTTP_404_NOT_FOUND)
		
		#we need a serializer when creating a post object
		serializer = UsersSerializer(model, data=request.data)  # we provide our data
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
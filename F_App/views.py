from django.http import HttpResponse
from django.shortcuts import render

from F_App.models import Car
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from F_App.serializers import UserSerializer


def hello_view(request):
    return HttpResponse("hello world ")

def create_car(request):
    car = Car(brand='demo', model='demo', color='demo')
    car.save()
    return HttpResponse(f'Yes!, New_car: {car.brand}')

@api_view(['GET'])
def demo(request):
    data = {'message': 'Hello'}
    return Response(data)


class UserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Car

# Create your views here.


class CarView(APIView):

    def get(self, request):
        car_obj = Car.objects.get(id=1)
        return Response(model_to_dict(car_obj))


class Car2View(APIView):

    def get(self, request):
        car_obj = Car.objects.get(id=2)
        return Response(model_to_dict(car_obj))

    def post(self, request):
        car_obj = Car.objects.get(id=2)
        car_obj.color = request.data['color']
        return Response(model_to_dict(car_obj))

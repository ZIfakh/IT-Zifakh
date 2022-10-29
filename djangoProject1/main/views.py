from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from main.models import CalcsHistory

# Create your views here.


class CalcsHistory_v(APIView):

    def get(self, request):
        calc_obj = CalcsHistory.objects.get(id=1)
        return Response(model_to_dict(calc_obj))


class CalcsHistory_c(APIView):

    def get(self, request):
        calc_obj = CalcsHistory.objects.get(id=1)
        return Response(model_to_dict(calc_obj))

    def post(self, request):
        cal_obj = CalcsHistory.objects.get(id=1)
        cal_obj.val1 = request.data['val1']
        cal_obj.val2 = request.data['val2']
        cal_obj.operator = request.data['operator']
        #cal_obj.val1 + cal_obj.val2 = data['result']
        request.data['result'] = cal_obj.val1  cal_obj.val2
        cal_obj.save()
        return Response(model_to_dict(cal_obj))

class Test_v(View):

    def get(self, request):
        cal_obj = CalcsHistory.objects.filter(id=1)
        return render(request, "list.html", {"list": cal_obj})

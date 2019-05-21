# _*_ coding:utf-8 _*_
from django.shortcuts import render

# Create your views here.
def get_tsp_aco_form(request):
    return render(request, 'tsp_aco_form.html')
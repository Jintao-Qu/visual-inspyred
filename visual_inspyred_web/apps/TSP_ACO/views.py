# _*_ coding:utf-8 _*_
from django.shortcuts import render

# Create your views here.
def get_tsp_aco_form(request):
    if request.method == "POST":
        post_dict = {}
        post_dict["dataset"] = request.POST.get("dataset", 'att48.tsp')
        post_dict["populations"] = request.POST.get("populations", '20')
        post_dict["iterations"] = request.POST.get("iterations", '100')
        print(post_dict)
    return render(request, 'tsp_aco_form.html')
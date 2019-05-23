# _*_ coding:utf-8 _*_
from django.shortcuts import render, redirect
from algorithms.tsp import tsp_aco,config
import _thread
# Create your views here.
def get_tsp_aco_form(request):
    if request.method == "POST":
        post_dict = {}
        config._init()
        post_dict["dataset"] = request.POST.get("dataset", 'att48.tsp')
        post_dict["populations"] = request.POST.get("populations", '20')
        post_dict["iterations"] = request.POST.get("iterations", '100')
        post_dict["biats"] = request.POST.get("biats", '100')
        print(post_dict)
        config.set_value("dataset", post_dict["dataset"])
        config.set_value("populations", post_dict["populations"])
        config.set_value("iterations", post_dict["iterations"])
        config.set_value("biats", post_dict["biats"])
        config.set_value("Generation", 0)
        config.set_value("Evaluation", 0)
        config.set_value("Worst", 0)
        config.set_value("Best", 0)
        config.set_value("Median", 0)
        config.set_value("Average", 0)
        config.set_value("Std_Dev", 0)
        config.set_value("Best_solution", "--")
        _thread.start_new_thread(tsp_aco.main, (1,))


        #tsp_aco.main()
        return redirect('/output/')
    else:
        return render(request, 'tsp_aco_form.html')
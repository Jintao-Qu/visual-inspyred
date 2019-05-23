from django.shortcuts import render
from django.shortcuts import render, redirect
from algorithms.tsp import config
# Create your views here.
def output(request):
    if request.method == "GET":

        return render(request, 'output.html', {
            'Generation': config.get_value("Generation"),
            'Evaluation': config.get_value("Evaluation"),
            'Worst': config.get_value("Worst"),
            'Best': config.get_value("Best"),
            'Median': config.get_value("Median"),
            'Average': config.get_value("Average"),
            'Std_Dev': config.get_value("Std_Dev"),
            'Progress': min(100,int(float(config.get_value("Generation"))/min(float(config.get_value("iterations")), 2000)*100)),
            'Best_solution': config.get_value("Best_solution")
        })
from django.shortcuts import render

# Create your views here.
def get_overview(request):
    return render(request, 'overview.html')
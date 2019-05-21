"""visual_inspyred_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from apps.overview.views import get_overview
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^overview/$', TemplateView.as_view(template_name='overview.html'), name="overview"),
    re_path('^tsp_aco_form/$', TemplateView.as_view(template_name='tsp_aco_form.html'), name="tsp_aco_form"),
    re_path('^documentation/$', TemplateView.as_view(template_name='documentation.html'), name="documentation"),
    re_path('^01knapsack_ga_form/$', TemplateView.as_view(template_name='01knapsack_ga_form.html'), name="01knapsack_ga_form"),
    re_path('^motifmining_pso_form/$', TemplateView.as_view(template_name='motifmining_pso_form.html'), name="motifmining_pso_form"),
    re_path('^tsp_data/$', TemplateView.as_view(template_name='tsp_data.html'), name="tsp_data"),
    re_path('^01knapsack_data/$', TemplateView.as_view(template_name='01knapsack_data.html'), name="01knapsack_data"),
    re_path('^motifmining_data/$', TemplateView.as_view(template_name='motifmining_data.html'), name="motifmining_data"),
    re_path('^downloads/$', TemplateView.as_view(template_name='downloads.html'), name="downloads"),
    re_path('^about/$', TemplateView.as_view(template_name='about.html'), name="about")
]

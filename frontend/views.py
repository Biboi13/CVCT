from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse

from api.models import VCT,Individual,Organization,Prob_occur

from django.contrib import messages
from datetime import datetime

from django.views.generic import CreateView

from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView

import json

from django.db.models import Sum, Count

# Create your views here.

#routing
def index(request):
    return render(request, 'frontend/index.html')
#Show Tables
def manage_indv(request):
    indv_list = Individual.objects.all() #VCT.objects.all().filter(individual__indv_name="Bob")
    context ={
             'indv_list': indv_list,
        }
    return render(request, 'frontend/manage_indv.html',context)


def manage_org(request):

    org_list = Organization.objects.all()
    context ={
             'org_list': org_list,
        }
    return render(request, 'frontend/manage_org.html',context)

# def chart(request):
#     return render(request, 'frontend/chart.html')


#charts

def pie_chart(request):
    labels_chart2 = []
    data_chart2 = []

    queryset = VCT.objects.order_by('vct_active_users')[:5]
    
    for active_user in queryset:
        labels_chart2.append(active_user.vct_name)
        data_chart2.append(active_user.vct_active_users)
    
    return render(request, 'frontend/chart.html', {
        'labels_chart2': labels_chart2 ,
        'data_chart2':  data_chart2 ,
    })


#recommend Chart
def pie_chart_VCT_recommend(request):
    labels_1 = []
    data_1 = []

    q = Individual.objects.filter().values('inv_place').order_by('sum').annotate(sum=Count('inv_place'))
    
    for i in q :
        data_1.append((i['sum']))
        labels_1.append(i['inv_place'])

 
    return render(request, 'frontend/chart.html', {
        'labels_1': labels_1,
        'data_1': data_1,
    })

def bar_chart_internet_bandwidth(request):
    labels_2 = []
    data_2 = []

    q_1 = Individual.objects.filter().values('indv_recommend_vct').order_by('sum').annotate(sum=Count('indv_recommend_vct'))
    
    for i_1 in q_1 :
        data_2.append((i_1['sum']))
        labels_2.append(i_1['indv_recommend_vct'])

 
    return render(request, 'frontend/chart.html', {
        'labels_2': labels_2,
        'data_2': data_2,
    })


def indv_count (request):
    count_indv = Individual.objects.count();
    return render(request, 'frontend/chart.html', count_indv)
from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse

from api.models import VCT,Individual,Organization,Prob_occur

from django.contrib import messages
from datetime import datetime

from django.views.generic import CreateView

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# Create your views here.

#routing
def index(request):
    return render(request, 'frontend/index.html')
#Show Tables
def manage_indv(request):
    indv_list = Individual.objects.all()
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

def chart(request):
    return render(request, 'frontend/chart.html')


#charts

def pie_chart(request):
    labels = []
    data = []

    queryset = VCT.objects.order_by('vct_active_users')[:5]
    for active_user in queryset:
        labels.append(active_user.vct_name)
        data.append(active_user.vct_active_users)

    return render(request, 'chart.html', {
        'labels': labels,
        'data': data,
    })

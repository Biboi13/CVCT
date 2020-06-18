from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse

from api.models import VCT,Individual,Organization,Prob_occur

from django.contrib import messages
from datetime import datetime

from django.views.generic import CreateView

from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView

import datetime
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
   

    # individual_using_vct_q = Individual.objects.filter().values('indv_recommend_vct').order_by('sum').annotate(sum=Count('indv_recommend_vct'))
    
    # chart 1
    indv_started_labels = []
    indv_started_data = []
    individual_started_q= Individual.objects.filter().\
                    values('indv_started_using_vct_name').order_by('indv_started_using_vct_name').\
                    annotate(sum=Count('indv_used_vct'))
    
    for i in individual_started_q:
        indv_started_labels.append(str(i['indv_started_using_vct_name']))
        indv_started_data.append(i['sum'])


    # chart 2
    org_started_labels = []
    org_started_data = []
    organization_started_q= Organization.objects.filter().\
                    values('org_started_using_vct_name').order_by('org_started_using_vct_name').\
                    annotate(sum=Count('org_used_vct'))
    
    for i in organization_started_q:
        org_started_labels.append(str(i['org_started_using_vct_name']))
        org_started_data.append(i['sum'])


    # chart 3
    chart_3_labels = indv_started_labels + org_started_labels
    chart_3_labels_sorted = sorted(chart_3_labels, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
    # print(chart_3_labels_sorted)


    # chart 4
    indv_prob_occur_q = Individual.objects.filter().\
                    values('indv_problem_occurred__probl_occur_name').order_by('indv_problem_occurred').\
                    annotate(sum=Count('indv_problem_occurred'))

    org_prob_occur_q = Organization.objects.filter().\
                    values('org_problem_occurred__probl_occur_name').order_by('org_problem_occurred').\
                    annotate(sum=Count('org_problem_occurred'))

    indv_prob_labels = []
    indv_prob_data = []
    for i in indv_prob_occur_q:
        indv_prob_labels.append(i['indv_problem_occurred__probl_occur_name'])
        indv_prob_data.append(i['sum'])

    org_prob_labels = []
    org_prob_data = []
    for i in org_prob_occur_q:
        org_prob_labels.append(i['org_problem_occurred__probl_occur_name'])
        org_prob_data.append(i['sum'])

    print(indv_prob_occur_q)
    print(org_prob_occur_q)

    total_indv = 0
    for i in indv_prob_occur_q:
        total_indv += i['sum']

    total_org = 0
    for i in org_prob_occur_q:
        total_org += i['sum']
    print(total_org)
    # chart 5
    indv_satisfactory_q = Individual.objects.filter().\
                    values('indv_satifactory').order_by('indv_satifactory').\
                    annotate(sum=Count('indv_satifactory'))

    indv_satis_labels = []
    indv_satis_data = []
    for i in indv_satisfactory_q:
        indv_satis_labels.append(i['indv_satifactory'])
        indv_satis_data.append(i['sum'])


    # chart 6
    indv_place_q = Individual.objects.filter().\
                    values('indv_place').order_by('indv_place').\
                    annotate(sum=Count('indv_place'))

    org_place_q = Organization.objects.filter().\
                    values('org_place').order_by('org_place').\
                    annotate(sum=Count('org_place'))
    
    indv_place_labels = []
    indv_place_data = []

    for i in indv_place_q:
        indv_place_labels.append(i['indv_place'])
        indv_place_data.append(i['sum'])

    org_place_labels = []
    org_place_data = []

    for i in org_place_q:
        org_place_labels.append(i['org_place'])
        org_place_data.append(i['sum'])



    # chart 7 
    indv_recom_q = Individual.objects.filter().\
                    values('indv_recommend_vct').order_by('indv_recommend_vct').\
                    annotate(sum=Count('indv_recommend_vct'))

    org_recom_q = Organization.objects.filter().\
                    values('org_recommend_vct').order_by('org_recommend_vct').\
                    annotate(sum=Count('org_recommend_vct'))


    context = {
        # graph 1
        'indv_started_labels': indv_started_labels,
        'indv_started_data': indv_started_data,

        # graph 2
        'org_started_labels': org_started_labels,
        'org_started_data': org_started_data,

        # graph 3
        'chart_3_labels': chart_3_labels_sorted,

        # graph 4
        'indv_prob_labels': indv_prob_labels,
        'total_indv': total_indv,
        'org_prob_labels': org_prob_labels,
        'total_org': total_org,


        # graph 5
        'indv_satis_labels': indv_satis_labels,
        'indv_satis_data': indv_satis_data,

     
        # graph 6
        'indv_place_labels': indv_place_labels,
        'indv_place_data': indv_place_data,

        'org_place_labels': org_place_labels,
        'org_place_data': org_place_data,


    }

    return render(request, 'frontend/chart.html', context=context)




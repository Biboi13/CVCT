from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manage_indv', views.manage_indv, name='manage_indv'),
    path('manage_org', views.manage_org, name='manage_org'),
    path('chart', views.chart, name='chart'),
    
    #chart
    path('pie-chart/', views.pie_chart, name='pie-chart'),

]

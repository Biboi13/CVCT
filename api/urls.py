from django.urls import path

from . import views

urlpatterns = [
        path('', views.apiOverview, name="api-overview"),
        path('VCT_list/', views.VCT_list, name="VCT_list" ),
        path('VCT_add/', views.VCT_add, name='VCT_add'),
        path('VCT_update/<str:pk>/', views.VCT_update, name="VCT_update"),
	    path('VCT_delete/<str:pk>/', views.VCT_delete, name="VCT_delete"),

        path('Prob_occur_list/', views.Prob_occur_list, name="Prob_occur_list" ),
        path('Prob_occur_add/', views.Prob_occur_add, name='Prob_occur_add'),
        path('Prob_occur_update/<str:pk>/', views.Prob_occur_update, name="Prob_occur_update"),
	    path('Prob_occur_delete/<str:pk>/', views.Prob_occur_delete, name="Prob_occur_delete"),

        path('Indv_list/', views.Indv_list, name="Indv_list" ),
        path('Indv_add/', views.Indv_add, name='Indv_add'),
        path('Indv_update/<str:pk>/', views.Indv_update, name="Indv_update"),
	    path('Indv_delete/<str:pk>/', views.Indv_delete, name="Indv_delete"),

        path('Org_list/', views.Org_list, name="Org_list" ),
        path('Org_add/', views.Org_add, name='Org_add'),
        path('Org_update/<str:pk>/', views.Org_update, name="Org_update"),
	    path('Org_delete/<str:pk>/', views.Org_delete, name="Org_delete"),
]
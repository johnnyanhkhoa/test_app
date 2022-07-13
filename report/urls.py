from argparse import Namespace
from django.urls import path, re_path
from report import views

app_name = 'report'
urlpatterns = [
    path('report_contract/<int:pk>/', views.report_contract, name='report_contract'),
    
    
]

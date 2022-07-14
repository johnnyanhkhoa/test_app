from argparse import Namespace
from django.urls import path, re_path
from report import views

app_name = 'report'
urlpatterns = [
    path('report_contract/<int:pk>/', views.report_contract, name='report_contract'),
    path('contract_follow_up/<int:pk>/', views.contract_follow_up, name='contract_follow_up'),
    
    
]

from argparse import Namespace
from django.urls import path, re_path
from quotation import views

app_name = 'quotation'
urlpatterns = [
    path('quotation-list-status/<int:pk>/', views.quotation_list_status, name='quotation_list_status'),
    path('quotation-list-channel/<int:pk>/', views.quotation_list_channel, name='quotation_list_channel'),
    path('search_quotation/', views.search_quotation, name='search_quotation'),
    path('quotation_update/<int:pk>/', views.quotation_update, name='quotation_update'),
    path('quotation_delete/<int:pk>/', views.quotation_delete, name='quotation_delete'),
    path('add_product_to_quotation/<int:pk>/', views.quotation_product_input, name='quotation_product_input'),
    path('quotation_product_delete/<int:pk>/', views.quotation_product_delete, name='quotation_product_delete'),
    path('quotation/<int:pk>/', views.final_quotation, name='final_quotation'),
    path('quotation_pdf/<int:pk>/', views.html_to_pdf_view, name='html_to_pdf_view'),
    path('contract/', views.contract, name='contract'),
    path('contract-list-status/<int:pk>/', views.contract_list_status, name='contract_list_status'),
    path('contract-list-channel/<int:pk>/', views.contract_list_channel, name='contract_list_channel'),
    path('search_contract/', views.search_contract, name='search_contract'),
    path('contract_update/<int:pk>/', views.contract_update, name='contract_update'),
    path('contract_delete/<int:pk>/', views.contract_delete, name='contract_delete'),
    
]

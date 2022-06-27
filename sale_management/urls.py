from django.urls import path
from sale_management import views

app_name = 'sale_management'
urlpatterns = [
    path('product_update/<int:pk>/', views.product_update, name='product_update'),
    path('product_delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('customer_update/<int:pk>/', views.customer_update, name='customer_update'),
    path('customer_delete/<int:pk>/', views.customer_delete, name='customer_delete'),
    path('customer_detail/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('product1/<int:pk>/', views.product1, name='product1'),
    path('product2/<int:pk>/', views.product2, name='product2'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('search_product/', views.search_product, name='search_product'),
    path('customer_channel_filter/<int:pk>/', views.customer_channel_filter, name='customer_channel_filter'),
    path('customer_type_filter/<int:pk>/', views.customer_type_filter, name='customer_type_filter'),
    path('customer_salearea_filter/<int:pk>/', views.customer_salearea_filter, name='customer_salearea_filter'),
    path('customer_province_filter/<int:pk>/', views.customer_province_filter, name='customer_province_filter'),
    path('search_customer/', views.search_customer, name='search_customer'),

]

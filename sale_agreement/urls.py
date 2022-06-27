from django.urls import path, include
from sale_agreement import views

app_name = 'sale_agreement'
urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup_changepassword, name='signup_changepassword'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    
]

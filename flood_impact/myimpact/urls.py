from django.urls import path

from myimpact import views


urlpatterns = [
        path('', views.index, name='index'),
        path('address_list/', views.address_list, name='address_list'),
        path('address_search/', views.address_search, name='address_search'),
        path('address/<str:address>/', views.address_detail, name='address_detail'),
    ]

from django.urls import path

from case import views

urlpatterns = [

    path('', views.add_case, name='add_case')
]
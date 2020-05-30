from django.urls import path

from case import views

urlpatterns = [

    path('add_case/', views.add_case, name='add_case')
]
from django.urls import path

from case import views

urlpatterns = [


    path('details/', views.Case_details_view, name='add_case')
]
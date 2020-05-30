from django.shortcuts import render

# Create your views here.
def add_case(request):
    return render(request, 'addcase.html')

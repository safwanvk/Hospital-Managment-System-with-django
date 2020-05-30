from django.shortcuts import render

# Create your views here.
from case.forms import CaseForm


def add_case(request):
    form = CaseForm
    context = {'form': form}
    return render(request, 'case/addcase.html', context)

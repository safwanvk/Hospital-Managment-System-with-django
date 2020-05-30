from django.shortcuts import render, redirect

# Create your views here.
from case.forms import CaseForm
from case.models import Case


def add_case(request):
    form = CaseForm
    cases = Case.objects.all()
    if request.method == 'Post':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_case')
    context = {'form': form, 'cases': cases}
    return render(request, 'case/addcase.html', context)

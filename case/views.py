from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from case.models import Case


class CaseCreateView(CreateView):
    model = Case
    fields = {
        'patient', 'description'
    }
    success_url = 'add_case'
    reverse_lazy = 'add_case'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['case'] = Case.object.get(id=1)
        return context()


def Case_details_view(request):
    case = Case.object.all()
    context = {
        'case': case
    }
    return render(render, 'case/casedetails.html')

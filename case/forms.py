from django import forms

from case.models import Case


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'patient', 'description'
        ]

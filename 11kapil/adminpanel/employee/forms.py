from django import forms
from .models import employe

class EmpForm(forms.ModelForm):
    class Meta:
        model = emplooye
        fields = "__all__"
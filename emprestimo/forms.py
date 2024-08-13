from django import forms
from . import models

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = models.Emprestimo
        fields = '__all__'
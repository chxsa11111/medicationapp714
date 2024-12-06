from django import forms
from .models import TodoModel, VaccinationTodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = "__all__"

class VaccinationTodoForm(forms.ModelForm):
    class Meta:
        model = VaccinationTodoModel
        fields = "__all__"

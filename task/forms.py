from django import forms
from . models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model =Task
        fields = "__all__"


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date',]
        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date'}  # HTML5 date picker
            )
        }
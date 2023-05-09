from django import forms
from .models import ToDoList

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name']

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    


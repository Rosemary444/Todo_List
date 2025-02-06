from django import forms
from todoapp.models import Todo

class todoform(forms.ModelForm):
  class Meta:
    model=Todo
    fields='__all__'


class editTask(forms.ModelForm):
  class Meta:
    model=Todo
    fields=['title','status']
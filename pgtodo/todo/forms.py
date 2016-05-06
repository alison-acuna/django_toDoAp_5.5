from django import forms

from .models import ToDo

class PostForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ('text',)

class DeleteForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = []

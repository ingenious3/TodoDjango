from django import forms
from .models import List

class ListForm(forms.ModelForm):

    def is_valid(self):
        prev = super(forms.ModelForm,self).is_valid()
        return True
    class Meta :
        model = List
        fields = ["item","completed"]
from django import forms

class abc(forms.Form):
    STRING = forms.CharField(widget=forms.Textarea)
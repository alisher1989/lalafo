from django import forms
from django.forms import widgets
from webapp.models import CATEGORY


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='name')
    description = forms.CharField(max_length=2000, required=True, label='description', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY, required=False, label='category')
    balance = forms.NumberInput()
    cost = forms.NumberInput()
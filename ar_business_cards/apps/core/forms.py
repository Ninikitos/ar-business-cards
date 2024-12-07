from django import forms
from .models import BusinessCard


class AddCardForm(forms.Form):
    model = BusinessCard
    fields = ['name', 'title', 'email', 'phone']
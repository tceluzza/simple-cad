from django import forms
from .models import Call

class CallForm(forms.Form):
  call_name = forms.CharField(label="Call name", max_length=64)
  call_notes = forms.Textarea()
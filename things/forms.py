from django import forms
"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
    name = forms.CharField(label='name')
    description = forms.CharField(label='description', widget=forms.Textarea)
    quatity = forms.CharField(label='quantity', widget=forms.NumberInput)
from django import forms

class BMICalculatorForm(forms.Form):
    height = forms.FloatField(label='Height (in cm)')
    weight = forms.FloatField(label='Weight (in kg)')

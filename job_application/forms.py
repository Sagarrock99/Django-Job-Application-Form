from django import forms
class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    dob = forms.DateField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
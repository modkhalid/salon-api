from django import forms
from .models import Saloon
class SaloonForm(forms.ModelForm):
    class Meta():
        model=Saloon
        fields=["name","ad_first","ad_second","city","country","pincode","image","password","email"]

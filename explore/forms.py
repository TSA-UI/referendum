from django import forms
from .models import Menu

class MenuFilterForm(forms.Form):
    menu = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'menu'}))
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'category'}))
    price = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'price'}))
    restaurant= forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'restaurant Name'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'city'}))
    specialize = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'specialization'}))
    rating = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'rating'}))

class AddMenuForm(forms.Form):
   class Meta:
       model = Menu
       fields = ['menu', 'category', 'restaurant_name', 'image', 'city', 'price', 'rating', 'specialized', 'takeaway', 'delivery', 'outdoor', 'smoking_area', 'wifi']
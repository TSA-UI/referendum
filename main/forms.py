from django.forms import ModelForm
from main.models import MenuItem

class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = [
            "menu", 
            "category", 
            "restaurant_name", 
            "image", 
            "city", 
            "price", 
            "rating", 
            "specialized", 
            "takeaway", 
            "delivery", 
            "outdoor", 
            "smoking_area", 
            "wifi"
        ]
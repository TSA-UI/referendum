from .models import Menu
import django_filters

class MenuFilter(django_filters.FilterSet):
    class Meta:
        model = Menu
        fields = ['menu', 'category', 'price', 'restaurant_name', 'city', 'price', 'rating', 'specialized']
        
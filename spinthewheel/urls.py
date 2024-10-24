from django.urls import path
from spinthewheel.views import menu_view, add_spin_history

app_name = 'spinthewheel'

urlpatterns = [
    path('', menu_view, name='menu_view'),
    path('add_spin_history/', add_spin_history, name='add_spin_history'),
]


from django.urls import path
from main.views import show_main
from spinthewheel.views import spin_wheel_view, spin_wheel, spin_history, add_to_options

app_name = 'spinthewheel'

urlpatterns = [
    # path('', show_main, name='show_main'),
    path('', spin_wheel_view, name='spin_wheel_view'),
    path('spin/', spin_wheel, name='spin_wheel'),
    path('history/', spin_history, name='spin_history'),
    path('add-to-options/<int:menu_id>/', add_to_options, name='add_to_options'),
]


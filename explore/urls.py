from django.urls import path
from explore.views import get_menu, show_menu, menu_detail

app_name = "explore"

urlpatterns = [
    #path("", get_menu, ),
    path("", show_menu, name='show_menu'),
    path("", menu_detail, name='menu_detail'),
]
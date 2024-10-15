# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Menu
from .forms import MenuFilterForm
from django.http import HttpResponse
from django.core import serializers

from .models import Menu

# Create your views here.
def show_menu(request):
    # user = request.user
    # user_profile = user.objects.get(user=user)

    # if user_profile.user_type.casefold() == "Admin":
    #     menu_list = serializers.serialize('json', Menu.objects.all())
    #     menu_list = serializers.deserialize('json', menu_list)
    #     menu_list = [menu.object for menu in menu_list]

    #     return render(request, 'admin_katalog.html', {'explore': menu_list})

    menus = Menu.objects.all()
    form = MenuFilterForm(request.GET)

    if form.is_valid():
        menu_name = form.cleaned_data.get("menu")
        kategori = form.cleaned_data.get("category")
        harga = form.cleaned_data.get("price")
        restaurant = form.cleaned_data.get("restaurant")
        kota = form.cleaned_data.get("city")
        specialization = form.cleaned_data.get("specialize")
        rate = form.cleaned_data.get("rating")

        if menu_name:
            menus = menus.filter(menu__icontains=menu_name)

        if kategori:
            menus = menus.filter(category__icontains=kategori)

        if harga:
            menus = menus.filter(price=harga)

        if restaurant:
            menus = menus.filter(restaurant_name__icontains=restaurant)

        if kota:
            menus = menus.filter(city__icontains=kota)

        if specialization:
            menus = menus.filter(specialized__icontains=specialization)

        if rate:
            menus = menus.filter(rating=rate)

    context = {
        'form': form,
        'explore': menus,
    }

    return render(request, 'menu.html', context)

def menu_detail(request, menu_id):
    # user = request.user
    menu = get_object_or_404(Menu, id=menu_id)
    context = {'menu': menu}
    return render(request, 'menu_detail.html', context)

def get_menu(request):
    data = Menu.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
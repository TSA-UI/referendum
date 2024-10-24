# Create your views here.
import json
from django.shortcuts import render,redirect, get_object_or_404
from .models import Menu
from .forms import MenuFilterForm
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


from .models import Menu

# Create your views here.
# @login_required(login_url="authentication:login")
def show_menu(request):
    user = request.user
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
    menu = get_object_or_404(Menu, id=menu_id)
    context = {'menu': menu}
    return render(request, 'menu_detail.html', context)

def add_menu(request):
    if request.method == "POST":
        menu = request.POST.get('menu')
        category = request.POST.get('category')
        restaurant_name = request.POST.get('restaurant_name')
        city = request.POST.get('city')
        price = request.POST.get('price')
        rating = request.POST.get('rating')
        specialized = request.POST.get('specialized')
        takeaway = request.POST.get('takeaway')
        delivery = request.POST.get('delivery')
        outdoor = request.POST.get('outdoor')
        smoking_area = request.POST.get('smoking_area')
        wifi = request.POST.get('wifi')
        image = request.POST.get('image')

        new_menu = Menu(menu=menu, category=category, restaurant_name=restaurant_name, city=city, 
                        price=price, rating=rating, specialized=specialized, takeaway=takeaway, delivery=delivery, 
                        outdoor=outdoor, smoking_area=smoking_area, wifi=wifi, image=image)
        new_menu.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_menu(request):
    data = Menu.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_menu_by_id(request, id):
    data = Menu.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_to_cart(request, menu_id, user_id):
    user =  get_object_or_404(User, id=user_id)
    menu = get_object_or_404(Menu, id=menu_id)
    user.cart.add(menu)
    return redirect('explore:show_menu')

@csrf_exempt
def filter_menu(request):
    menu_name = request.GET.get('menu', '')
    kategori = request.GET.get('category', '')
    harga = request.GET.get('price', None)
    restaurant = request.GET.get('restaurant', '')
    kota = request.GET.get('city', '')
    specialization = request.GET.get('specialize', '')
    rate = request.GET.get('rating', None)

    menus = Menu.objects.all()
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
    menu_json = serializers.serialize('json', menus)
    return JsonResponse(menu_json, safe=False)
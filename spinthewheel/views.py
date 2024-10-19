from django.shortcuts import render, redirect
from .models import Menu, Option, SpinHistory
import random
import json
from django.http import JsonResponse

def menu_view(request):
    category = request.GET.get('category', None)
    if category:
        menu_items = Menu.objects.filter(category=category)
    else:
        menu_items = Menu.objects.all()

    options = Option.objects.all()
    context = {
        'menu_items': menu_items,
        'options': options,
        'category': category,
    }
    return render(request, 'menu.html', context)

# API to add items to the options (AJAX request)
def add_to_options(request, menu_id):
    menu_item = Menu.objects.get(id=menu_id)
    Option.objects.create(menu=menu_item)
    return JsonResponse({"status": "success", "menu_name": menu_item.name})

# API to handle the spinning action
def spin_wheel_view(request):
    menu_items = Menu.objects.all()  # Get all menu items
    categories = Menu.objects.values_list('category', flat=True).distinct()  # Get unique categories
    spin_history = SpinHistory.objects.all().order_by('-spin_time')  # Get spin history

    context = {
        'menu_items': menu_items,
        'categories': categories,
        'spin_history': spin_history,
    }
    return render(request, 'spinthewheel.html', context)

def spin_wheel(request):
    options = Option.objects.all()
    if options:
        selected_option = random.choice(options)
        SpinHistory.objects.create(selected_option=selected_option.menu)
        Option.objects.all().delete()  # Clear options after spin
        return JsonResponse({"winner": selected_option.menu.name})
    return JsonResponse({"winner": None})
    
# History view
def spin_history(request):
    spin_history = SpinHistory.objects.all().order_by('-spin_time')
    return render(request, 'spin_history.html', {'spin_history': spin_history})

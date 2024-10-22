from django.shortcuts import render
from explore.models import Menu
from .models import Option, SpinHistory
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse

@login_required(login_url='/login')
def menu_view(request):
    # Default selected category is 'All Categories'
    category = request.POST.get('category', 'All Categories')
    categories = ['All Categories', 'Beef', 'Chicken', 'Fish', 'Lamb', 'Pork', 'Rib Eye', 'Sirloin', 'Tenderloin', 'T-Bone', 'Wagyu', 'Other']

    # Filter menu items based on selected category
    if category != 'All Categories':
        menu_items = Menu.objects.filter(category=category)
    else:
        menu_items = Menu.objects.all()

    for menu_item in menu_items:
        Option.objects.get_or_create(menu=menu_item)

    options = Option.objects.filter(menu__in=menu_items)

    context = {
        'menu_items': menu_items,
        'categories': categories,
        'selected_category': category,
        'options': options, 
    }
    
    return render(request, 'lmao.html', context)

@csrf_exempt
@require_POST
def add_spin_history(request):
    winner = request.POST.get("winner")
    user = request.user

    # Create new SpinHistory entry
    if winner:
        spin_history = SpinHistory(
            user=user,
            winner=winner,
        )
        spin_history.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponse(b"BAD REQUEST", status=400)
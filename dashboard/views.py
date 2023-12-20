from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def videos_list(request):
    return render(request, "dashboard/videos-list.html")

def blank_page(request):
    return render(request, "dashboard/blank-page.html")

def badges(request):
    return render(request, "dashboard/badges.html")

def buttons(request):
    return render(request, "dashboard/buttons.html")

def cards(request):
    return render(request, "dashboard/cards.html")

def card_actions(request):
    return render(request, "dashboard/card-actions.html")

def cards_masonry(request):
    return render(request, "dashboard/card-masonry.html")

def colors(request):
    return render(request, "dashboard/colors.html")

def form_elements(request):
    return render(request, "dashboard/form-elements.html")

def login(request):
    return render(request, "login.html")

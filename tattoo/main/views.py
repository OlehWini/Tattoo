from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .models import Master


# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


def blog_page(request):
    return render(request, 'main/blog.html', {})


def masters_page(request):
    masters = Master.objects.all()
    return render(request, 'main/masters.html', {'masters':masters})

def search_master(request):
    search_masters =[]
    masters = Master.objects.all()
    if request.method == 'POST':
        search_character = request.POST.get('f_for_search')
        for master in masters:
            if search_character.upper() == master.city.upper():
                search_masters.append(master)

            elif search_character.upper() == master.name.upper():
                search_masters.append(master)
            elif search_character.upper() == master.sur_name.upper():
                search_masters.append(master)
    return render(request, 'main/searchMastersResult.html', {'search_masters':search_masters})

def shop_page(request):
    return render(request, 'main/shop.html', {})


def login(request):
    return render(request, 'main/login.html', {})


def regist_new_user(request):
    return render(request, 'main/registration.html')
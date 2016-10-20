from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from .models import Article
from .models import Master
from  django.template import Context
from .models import Topic, Comments
from forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles,'username': auth.get_user(request).username})


def blog_page(request):
    topics = Topic.objects.all()
    return render(request, 'main/blog.html', {'topics':topics,'username': auth.get_user(request).username})

def topic_blog_page(request, topic_id=1):
    topic = Topic.objects.get(id=topic_id)
    comments = Comments.objects.filter(topic_id=topic_id)
    # comments = Comments.objects.get(topic_id=topic_id)
    return  render(request, 'main/topic_in_blog.html', {'topic':topic,'comments':comments, 'username':auth.get_user(request).username})

def add_record(request, topic_id=1):
    topic22=Topic.objects.get(id=topic_id)
    if request.method =='POST':
        Comments.objects.create(
            comments_text_of_comment=request.POST.get('fCommentText'),
            topic = topic22,
            username=auth.get_user(request).username
        )

    context = {
        'username':username
    }
    return render(request, 'main/topic_in_blog.html', context)


def show_record(request):
    return render(request, 'main/topic_in_blog.html', {})


def masters_page(request):
    masters = Master.objects.all()
    return render(request, 'main/masters.html', {'masters':masters, 'username': auth.get_user(request).username})


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
    return render(request, 'main/searchMastersResult.html', {'search_masters':search_masters, 'username': auth.get_user(request).username})


def shop_page(request):
    return render(request, 'main/shop.html', {'username': auth.get_user(request).username})


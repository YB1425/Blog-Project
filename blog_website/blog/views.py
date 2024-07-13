from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import UserTable
from .models import PostTable
from .models import PostCategory
from .models import Comment
def users(request):
    myusers = UserTable.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers' : myusers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def posts(request):
 all_posts = PostTable.objects.all().values()
 template = loader.get_template('blogs.html')
 context = {
        'all_posts' : all_posts,
    }
 return HttpResponse(template.render(context, request))

def categories(request):
    all_categories = PostCategory.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'all_categories': all_categories,
    }
    return HttpResponse(template.render(context, request))



def post_detail(request, post_id):
    post = get_object_or_404(PostTable, pk=post_id)
    context = {
        'post' :post
    }
    return render(request,'blogdetails.html',context)

def comments_fetch(request):
    comments = Comment.objects.select_related('post').all()
    context = {
        'comments': comments,
    }

    return render(request, 'comments.html', context)

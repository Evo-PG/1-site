from django.shortcuts import render
from .models import Post, Category


def homes_site(reqeust):
    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request=reqeust, template_name="app/home.html", context={"posts": posts,"categories":categories})

def post_description(request, pk):
    posts = Post.objects.get(id=pk)
    categories = Category.objects.all()

    return render(request=request, template_name="app/description.html", context={"posts": posts,"categories":categories})

def category_sort(reqeust, pk):
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()

    return render(request=reqeust, template_name="app/category_sort.html", context={"posts":posts,"categories":categories})

def developer(reqeust):
    categories = Category.objects.all()

    return render(request=reqeust, template_name="app/developer.html", context={"categories":categories})


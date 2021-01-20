from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  django.utils import timezone


# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

#!Index Page
def index(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

#!About Page
def about(request):
    return render(request, "about.html")

#!Contact
def contact(request):
    return render(request, "contact.html")

#!Dashboard
@login_required(login_url= "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles,
    }
    return render(request, "dashboard.html", context)

#!Detail
def detail(request,id):
    article = get_object_or_404(Article,id = id)
    return render(request,"detail.html",{"article":article})

#!Addarticle
@login_required(login_url= "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale basari Ile Eklendi")
        return redirect("article:dashboard")
    
    return render(request, "addarticle.html", {"form": form})

#!UPdateArticle
@login_required(login_url= "user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id= id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale Yenilendi")
        return redirect("article:dashboard")
    return render(request, "update.html", {"form": form})

#!DeleteArticle
@login_required(login_url= "user:login")
def deletArticle(request, id=id):
    article = get_object_or_404(Article, id=id)

    article.delete()
    messages.success(request, "Makale Basari ile silindi")

    return redirect("article:dashboard")

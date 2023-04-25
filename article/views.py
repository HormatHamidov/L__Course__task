from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def articles__page(request):
    keyword = request.GET.get('keyword')
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, 'articles.html',{"articles": articles})
    
    articles = Article.objects.all()
    return render(request, 'articles.html',{"articles": articles})

@login_required(login_url='user:login')
def dashboard__page(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        'articles': articles
    }
    return render(request, 'dashboard.html',context)


@login_required(login_url='user:login')
def addarticle__page(request):
    form = ArticleForm(request.POST or None, request.FILES)
    
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, 'Article added successfully')
        return redirect('home')
        
    return render(request, 'addarticle.html',{'form':form})


@login_required(login_url='user:login')
def detail__page(request, id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)
    return render(request, 'detail.html', {'article':article})


@login_required(login_url='user:login')
def update__page(request, id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Successfully updated article")
        return redirect("article:dashboard")
    return render(request, 'update.html', {'form':form})


def delete__page(request, id):
    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"Successfully deleted article")
    return redirect("article:dashboard")
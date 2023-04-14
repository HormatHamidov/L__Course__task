from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
from django.contrib import messages

# Create your views here.

def dashboard__page(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        'articles': articles
    }
    return render(request, 'dashboard.html',context)


def addarticle__page(request):
    form = ArticleForm(request.POST or None)
    
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, 'Article added successfully')
        return redirect('home')
        
    return render(request, 'addarticle.html',{'form':form})


def detail__page(request, id):
    article = Article.objects.filter(id = id).first()
    return render(request, 'detail.html', {'article':article})
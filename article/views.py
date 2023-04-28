from django.shortcuts import render, redirect, get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def articles__page(request):
    if keyword := request.GET.get('keyword'):
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
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    return render(request, 'detail.html', {'article':article,"comments":comments})


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


def comment__page(request,id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
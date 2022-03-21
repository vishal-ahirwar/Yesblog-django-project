from django.shortcuts import render,get_object_or_404
from .models import Post,Comments
from .forms import CommentClass
# Create your views here.


def Detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    form= CommentClass()
    com =Comments.objects.all()

    return render(request, "base/detail.html",{'posts':post,'form':form,'com':com   })
    


def HomePage(request):
    posts=Post.objects.all()

    return render(request, "base/frontpage.html",{"posts":posts})


def AboutPage(request):
    return render(request, "base/about.html")

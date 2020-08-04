from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from TestApp.models import Post, Comment, Feedback, Breaking
from TestApp.forms import CommentForm, FeedbackForm
# Create your views here.
def list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)

    return render(request,"TestApp/list.html",{"post_list":post_list})


def detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status="published",publish__year=year,publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,"TestApp/detail.html",{"post":post,"form":form,"comments":comments,"csubmit":csubmit})


def feedback_view(request):
    form=FeedbackForm()
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"TestApp/thankyou.html")
    return render(request,"TestApp/feedback.html",{"form":form})


def contact_view(request):
    return render(request,"TestApp/contact.html")

def about_view(request):
    return render(request,"TestApp/about.html")


def adm_view(request):
    return render(request,"TestApp/ss.html")

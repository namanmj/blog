from django.shortcuts import redirect, render,get_object_or_404
from .models import blog
from .forms import PostForm,NewUserForm
from django.utils import timezone
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
# Create your views here.

def blog_list(request):
    posts=blog.objects.all()
    return render(request,'post_list.html',{'posts':posts})

def detail_blog(request,pk):
    post=get_object_or_404(blog, pk=pk)
    return render(request,'detail.html',{'post':post})

@login_required(login_url='/login')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request,'create.html',{'form':form})

@login_required(login_url='/login')
def post_edit(request, pk):
    post = get_object_or_404(blog, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required(login_url='/login')
def post_delete(request,pk):
    post=get_object_or_404(blog,pk=pk)
    post.delete()
    return redirect('blog_list')

def register(request):
    if request.method == "POST":
	    form = UserCreationForm(request.POST)
	    if form.is_valid():
		    user = form.save()
		    login(request, user)
		    messages.success(request, "Registration successful." )
		    return redirect('blog_list')
	    messages.error(request, "Unsuccessful registration. Invalid information.")
    else:

        form = UserCreationForm()
    return render(request,'sign_up.html',{'form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        username=form.data['username']
        password=form.data['password']
        user = authenticate(request,username=username,password=password)
        login(request, user)
        if user is not None:
            return redirect('blog_list')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_request(request):
    logout(request)
    return redirect('blog_list')
    
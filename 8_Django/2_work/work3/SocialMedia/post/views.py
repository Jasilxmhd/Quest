from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm
from django .urls import reverse_lazy

from django.http import HttpResponse

# Email 

from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'postlist.html'
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    template_name = 'postcreate.html'
    fields = '__all__'
    context_object_name = 'posts'


class UpdatePost(UpdateView):
    model = Post
    template_name = 'postcreate.html'
    fields = ['title','description','image']


class DeletePost(DeleteView):
    model = Post
    template_name = 'postdelete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('list')



def post_list(request):
    posts = Post.objects.all()
    return render(request,'post/list.html',{'post':posts})

def post_create(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Post.objects.create(

            title = title,
            description = description,
            image = image
        )

        return redirect("post_list")
    return render(request,'post/create.html')



# Read
def post_list(request):
    posts=Post.objects.all()
    return render(request,"post/list.html",{'posts':posts})



# update
def post_update(request,id):
    post=get_object_or_404(Post,id=id)
    
    if request.method=="POST":
        post.title=request.POST.get("title")
        post.description=request.POST.get("description")
        
        if request.FILES.get("image"):
            post.image=request.FILES.get("image")
        post.save()
        
        return redirect("post_list")
    return render(request,"post/update.html",{"post":post})



# Delete
def post_delete(request,id):
    post =get_object_or_404(Post,id=id)
    
    if request.method=="POST":
        post.delete()
        return redirect("post_list")
    return render(request,"post/delete..html",{"post":post})






def send_html_email(request):
    subject = "welcome"
    text_content = "welcome to django"

    html_content = """

    <h1>welcome to Django</h1>
    <p>This is an <b> HTML email </p>
    """


    email = EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER,
        ['sreerajquest@gmail.com']
    )

    email.attach_alternative(html_content,"text/html")
    email.send()

    return HttpResponse("email send succesfully")


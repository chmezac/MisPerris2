from django.utils import timezone
from .models import Post, Dog, AdoptionRegister
from django.shortcuts import render, render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from blog.forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
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
    return render(request, 'blog/post_edit.html', {'form': form})    
    


def misperris(request):
    return render(request, 'blog/base.html', {})

def form1(request):
    return render(request, 'blog/formulario.html', {})

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(username=usuario,first_name=nombre,last_name=apellido, email=email, password=password_one, is_staff=True)
            u.save()
            return render(request, 'blog/welcome.html', {})
        else:
            ctx = {'form':form}
            return render(request, 'blog/usuario.html', ctx)
    ctx = {'form':form}
    return render(request, 'blog/usuario.html', ctx)

def loginview(request):
    url = "http://chmezac.pythonanywhere.com/admin"
    return redirect(url)

def dog_list(request):
    dogs= Dog.objects.filter(state="Disponible")
    return render(request, 'blog/formulario.html', {'dogs': dogs})    

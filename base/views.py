from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views.generic import DetailView,CreateView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import *
from .models import *

menu = [{'title':'О сайте','url_name':'about'},
        { 'title':'Добавить статью','url_name':'add_page'},
        {'title':'Обратная связь','url_name':'contact'},
        ]

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)


def index(request):
    posts = News.objects.all()
    cats = Category.objects.all()
    context = {
        'title':'Главная страница',
        'cats':cats,
        'menu': menu,
        'posts': posts,
        'cat_selected':0
    }
    return render(request,'base/index.html',context)

def about(request):
    context = {
        'title':'О нас',
        'menu': menu
    }
    return render(request,'base/about.html',context)


def show_category(request,cat_id):
    posts = News.objects.filter(cat_id = cat_id)
    cats = Category.objects.all()
    context = {
        'title': 'Отображение новостей',
        'cats': cats,
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id
    }

    return render(request,'base/index.html',context)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'base/addpage.html'
    success_url = reverse_lazy('main')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


class ShowPost(DetailView):
    model = News
    template_name = 'base/post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context



def contact(request):
    return HttpResponse('Обратная связь')



# import django system

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# import models

from .models import Post, Comment

# import forms

from .forms import PostForm, CommentForm

# Create your views here.

def community(request):
    post_model = Post.objects.all()

    context = {
        'post' : post_model,
    }

    return render(request, 'community.html', context)

def community_detail(request, post_id):
    post_model = Post.objects.get(pk=post_id)
    comment_model = Comment.objects.filter(post=post_model.title)

    context = {
        'post' : post_model,
        'comment' : comment_model,
    }
    return render(request, 'community_dtail.html', context)

def community_write(request):
    post_form = PostForm()
    context = {
        'form' : post_form,
    }
    if request.method == "POST":
        if not request.user.is_anonymous:
            if post_form.is_valid():
                post_form.save(commit=False)
                post_form.author = request.user
                post_form.save()
                return redirect('community')
    return render(request, 'community_write.html', context)



""" class community(ListView):
    template_name = 'community.html'
    context_object_name = 'blog_list' 
    def get_queryset(self):
        return Blog.objects.all

class community_view(DetailView):
    model = Blog
    template_name = 'community_view.html'
    context_object_name = 'blog'

class community_delete(DeleteView):
    model = Blog
    template_name = 'community_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('community')

class community_update(UpdateView):
    model = Blog
    template_name = 'community_update.html'
    fields = ['title','text']
    success_url = reverse_lazy('community')

class community_write(CreateView):
    model=Blog
    template_name='community_write.html'
    fields=['title','text']

    def form_valid(self,form):
        Blog=form.save(commit=False)
        Blog.author=self.request.user
        Blog.save()

        return HttpResponseRedirect(self.request.POST.get('next','/'))

def comment_write(request, post_pk):
    if request.method == 'POST':
        post=get_object_or_404(Blog, pk=post_pk)
        content=request.POST.get('comment_contents')
        context = {
            'post_pk' : post_pk
        }

        Comment.objects.create(post=post, comment_write=writer,comment_contents=content)
        return HttpResponseRedirect(reverse_lazy('community', context)) """
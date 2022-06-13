from audioop import reverse
import imp
from multiprocessing import context
from os import access
from unicodedata import category
from urllib import request
from xml.etree.ElementTree import Comment
# get a object if it doesn't exist return or a 404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from myblog.models import Post
from .models import Post, Category, Comment
from .form import CommentForm, PostForm, EditForm
from django.urls import reverse_lazy, reverse


# def home(request):
#     return render(request, 'home.html', {})

# we need to save that to the database and we need to know which post we talk about here then we need to save it
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # bat cu thu j tu post_id dc click
    # after click this is sends the post id then add a like for wev user
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
    # post_id: button in article_details named post_id
    # we're filling out a form and we're summitting it and when we submit it we can grab something from flat form by calling request.post,
    # I get and then calling the post ID


def UnLikeView(request, pk):
    post = get_object_or_404(Post)


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
# pass the request to urls and urls get passed and URL is going to be cats(key)

# create code that passes context dictionary into our page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        # push cat_menu on the page as a context dictionary that we can access
        # stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        # total_likes = stuff.total_likes()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        # context["total_likes"] = total_likes
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})
# query database -> grabbing all of our category name -> assining to variable -> passing that variable into our context dictionary


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
    #cats.title(): make uppercase #

# it take to pass something in contextually into your page, all thing in bracket also passe the thing
# you have to do whole a lot of other code in order to do that for class-based views


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        # push cat_menu on the page as a context dictionary that we can access
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'  # put all field in this page
    # # fields = ('title', 'body')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    # fields = '__all__'
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        # it tell that there's a user filling out this form let't grab that user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'title_tag', 'body')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

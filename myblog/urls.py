from django.shortcuts import redirect
from django.urls import path

from myblog.models import Post
# from . import views
from .views import HomeView, AddPostView, ArticleDetailView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(),
         name='article-detail'),  # go to ArticleDetailView by id, primary key
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add_comment"),


]


# No URL to redirect to. Provide a success_url
# because it's trying to redirect somewhere after we delete and it doesn't know where
# truoc day chuyen ve hom trong model
# can phai noi chinh xac noi can den and we can't use the 'reverse' thing

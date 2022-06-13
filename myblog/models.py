from audioop import reverse
from turtle import title
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # point this back to the article details page
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # if delete our user all of theuser profile stuff will also get deleted
    # user model is in our Django authentication
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True,)
    twitter_url = models.CharField(max_length=255, null=True, blank=True,)
    instagram_url = models.CharField(max_length=255, null=True, blank=True,)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True,)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        # tell that what article detail page to go to
        return reverse('home')
        # we could also have it go back to the main page
        # 'article-detail', args=(str(self.id))


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    # install pillow who is image library
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    # defaut for a bunch of blog post already
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(
        max_length=255)

    likes = models.ManyToManyField(User, related_name='blog_posts')
    # this allows us to associate different things from different tables EX: post have many likes
    # gave them a related name called blog posts

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)  # formatting for admin

    def get_absolute_url(self):
        # tell that what article detail page to go to
        return reverse('home')
        # we could also have it go back to the main page
        # 'article-detail', args=(str(self.id))


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # tell that what article detail page to go to
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '%s - %s' % (self.post.title, self.name)


# order blog by date: tao field model => push migration => them field vao html

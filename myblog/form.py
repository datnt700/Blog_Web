from dataclasses import field
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from . models import Post, Category, Comment

# cats = [('coding', 'coding'), ('sports', 'sports'),
#         ('entertainment', 'entertainment')]
# double that how select box work: one for remmember, the other is the thing to show
# modelform allows us to create fields for our model in this case
# grap a specific list of value from there
choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'snippet', 'header_image')

        widgets = {  # add styling
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'elder'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,
                                     attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag',
                  'body', 'snippet', 'header_image')

        widgets = {  # add styling
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})

        }

# To Create EditForm start form.py = create new class name => import it to view.py


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {  # add styling
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

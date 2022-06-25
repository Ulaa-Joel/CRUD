# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dataclasses import field, fields

from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, TemplateView

# Create your views here.
def PostListView(ListView):
    model = Post

def PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

def PostDetailView(DetailView):
    model = Post

def PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

def PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
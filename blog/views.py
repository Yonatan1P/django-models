from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    model = Blog

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = Blog
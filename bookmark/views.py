from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

class BokkmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark
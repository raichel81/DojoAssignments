# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
  # the index function is called when root is visited
def index(request):
    return render(request, "blogs/index.html")

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print request.POST['name']
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

def new(request):
    return render(request, "blogs/index.html")

def show(request, number):
    response = "placeholder to display blog ", number
    return HttpResponse(response)

def edit(request, number):
    response =  "placeholder to edit blog ", number
    return HttpResponse(response)

def delete(request, number):
    return redirect('/blogs')
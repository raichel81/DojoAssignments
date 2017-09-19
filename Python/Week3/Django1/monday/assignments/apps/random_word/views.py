# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counts' not in request.session:
        request.session['counts'] = 1
    else:
        request.session['counts'] += 1
    context = {
    "counts": request.session['counts'],
    "word": get_random_string(length=14)
    }
    return render(request, "random_word/index.html", context)

def reset(request):
    request.session.clear()
    return redirect("http://localhost:8000/random_word/")

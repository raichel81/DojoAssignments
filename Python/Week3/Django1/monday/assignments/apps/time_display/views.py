# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
def index(request):
    context = {
    "time": strftime("%d %b %Y %I:%M%p", localtime())
    }
    return render(request, "time_display/index.html", context)
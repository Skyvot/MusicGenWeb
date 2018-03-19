# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def hello(request):
    return render(request, "index.html")


def download(request):
    return render(request, "test.html")

from django.http import FileResponse


def file_down(request, mood):
    if mood == "Mood":
        return render(request, "test.html")
    else:
        file = open('static/'+mood+'.mid', 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename="+mood+'.mid'
        return response

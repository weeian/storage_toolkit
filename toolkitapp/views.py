# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import FileResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def file_down(request):
    file=open('/home/amarsoft/download/example.tar.gz','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="example.tar.gz"'
    return response
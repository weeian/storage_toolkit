# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.shortcuts import render
from django.http import FileResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

# 下载authBucket手册
def get_ab_manual(request):
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/ABManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="ABManual.html"'
    return response

# 下载BaseApiTest手册
def get_bat_manual(request):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/BATManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="BATManual.html"'
    return response

# 下载cosbench手册
def get_cos_manual(request):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/CosManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="CosManual.html"'
    return response

# 下载fio手册
def get_fio_manual(request):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/FioManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="FioManual.html"'
    return response

# 下载ior手册
def get_ior_manual(request):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/IorManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="IorManual.html"'
    return response

# 下载mdtest手册
def get_md_manual(request):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/MDManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="MDManual.html"'
    return response

# 下载obs-test手册
def get_ot_manual(request):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/OTManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="OTManual.html"'
    return response

# 下载vdbench手册
def get_vd_manual(request):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(root_path+'/toolkitapp/resource'
                '/manual/VDManual.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="VDManual.html"'
    return response

# 访问fio页面
def fio(request):
    return render(request, 'fio.html')

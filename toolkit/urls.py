"""toolkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from toolkitapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/', views.index, name='index'),

    url(r'toolkitapp/resource/manual/ABManual.html', views.get_ab_manual, name='get_ab_manual'),
    url(r'toolkitapp/resource/manual/IorManual.html', views.get_ior_manual, name='get_ior_manual'),
    url(r'toolkitapp/resource/manual/CosManual.html', views.get_cos_manual, name='get_cos_manual'),
    url(r'toolkitapp/resource/manual/VDManual.html', views.get_vd_manual, name='get_vd_manual'),
    url(r'toolkitapp/resource/manual/MDManual.html', views.get_md_manual, name='get_md_manual'),
    url(r'toolkitapp/resource/manual/ABManual.html', views.get_ab_manual, name='get_ab_manual'),
    url(r'toolkitapp/resource/manual/OTManual.html', views.get_ot_manual, name='get_ot_manual'),
    url(r'toolkitapp/resource/manual/BATManual.html', views.get_bat_manual, name='get_bat_manual'),

    url(r'fio/', views.fio, name='fio'),



]

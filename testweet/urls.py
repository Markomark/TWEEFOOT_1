"""testweet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include
from TWEET import views as myapp_views
		
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url	(r'^AS/(?P<depute>\w{0,50})$', myapp_views.depute, name = "depute"),	
	url	(r'^TOP/(?P<sort>\w{0,50})/(?P<periode>\w{0,50})/$', myapp_views.top, name = "top"),
	url	(r'^LIST/(?P<sort>\w{0,50})/$', myapp_views.ann, name = "ann"),	
	url	(r'^TL/$', myapp_views.parti, name = "parti"),	
	url(r'^', myapp_views.index, name = "index"),
    url(r'^admin/', include(admin.site.urls)),
]

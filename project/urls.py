"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.generic import View 


class MyCBV(View ):
    def get(self,request):
        return HttpResponse(' this is saror saad create CBV')
    
    

  
   


def myfbv(request):
    return HttpResponse(' this is saror saad create FBV')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv/',myfbv),
    path('',MyCBV.as_view())
]

'''
path function take at least tow arguments :
1- name of url  ex=contact,profile and end with slash /
2-view: either function or class which take http request and return http 
response    --->path('contact/' ,view)
NB:view may  take inderect url or url module instead of  direct fuction or class ---> path('contact/' ,urls_module)
        ----->path('contact/' ,urls_urlpatterns)

'''
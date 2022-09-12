
from django.contrib import admin
from django.urls import path
from posts.views import all_posts,single_post
# from django.http import HttpResponse
# from django.views.generic import View 


# class MyCBV(View ):
#     def get(self,request):
#         return HttpResponse(' this is saror saad create CBV')   


# def test1(request):
#     my_response =  """ 
   
#     <h1> my name is <span  style ='color:red'> saror </span>  </h1>
#      <h1> i am  <span style ='color:red'> radiologist </span>  </h1>
#     """
#     return HttpResponse( my_response)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',all_posts,name='all_posts'),
    path('blog/<int:id>',single_post,name='single_post'),
#     path('',MyCBV.as_view())
]

'''
path function take at least tow arguments :
1- name of url  ex=contact,profile and end with slash /
2-view: either function or class which take http request and return http 
response    --->path('contact/' ,view)
NB:view may  take inderect url or url module instead of  direct fuction or class ---> path('contact/' ,urls_module)
        ----->path('contact/' ,urls_urlpatterns)

'''
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView


from . import views

urlpatterns = [
    url(r'^$', views.lesson_list, name='lesson_list'),
    url(r'^(?P<urok_slug>[-\w]+)/$',
        views.lesson_list,
        name='lesson_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.lesson_detail,
        name='lesson_detail'),
    url('post/',views.createpost,name='createpost'),
    url('personal/',views.personal,name='personal'),
    url('logout/',views.logout,name='logout'),
     
    url(r'^update/(?P<id>\d+)/$', views.update_view,name='update_view'),  
    url(r'^delete/(?P<id>\d+)/$', views.delete_view,name='delete_view'),
    
    
    
    
    
    

    
    
    
    
    
    
] 
LOGIN_REDIRECT_URL = r'^$'
from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.cache import never_cache
from django.contrib.contenttypes.models import ContentType
from .models import Urok , Lesson
from django.contrib.auth.decorators import permission_required, login_required,user_passes_test
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.html import format_html
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
from .forms import GeeksForm


# Create your views here.


@login_required(login_url='login/')









def lesson_list(request, urok_slug=None):
    query = request.GET.get('search')
    if query:
        lessonse = Lesson.objects.filter(name__icontains=query)
        return render(request,'search/search_results.html',{'lessonse':lessonse})
    

   
    urok = None
    
    uroks = Urok.objects.all()
    lessons = Lesson.objects.filter(available=True)
    
    if urok_slug:
        urok = get_object_or_404(Urok, slug=urok_slug)
        lessons = lessons.filter(category_id=urok)
    return render(request,
                  'product/list.html',
                  {'urok': urok,
                   'uroks': uroks,
                   'lessons': lessons})
    

def lesson_detail(request, id, slug):
    lesson = get_object_or_404(Lesson,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'product/detail.html',
                  {'lesson': lesson})




def createpost(request):
    username = None
    uroks = Urok.objects.all()
    
    
    
    if request.user.is_authenticated:
        username = request.user
        if request.method == 'POST':
            if request.POST.get('name')  and request.POST.get('slug') and request.FILES.get('upload'):
                post=Lesson()
                post.name= request.POST.get('name')
                
                post.upload = request.FILES.get('upload')
                post.slug= request.POST.get('slug')
                
                
                
                
                query = request.POST.get('category')
                if query:
                    urk = Urok.objects.filter(name__icontains=query).first()
                    
                    post.category = urk
                    fs = FileSystemStorage()
                    filename = fs.save('upload',post.upload)
                    uploaded_file_url = fs.url("")
                   
                    
                    post.author= username
                    post.save() 
                
                return render(request,'personal/return.html')
                
                
                
                

        else:
                return render(request,'add/add.html',{'uroks': uroks,})
    return render(request,'add/add.html',{'uroks': uroks,})


def personal(request):
    username = None
    urok = None
    
    
    
    if request.user.is_authenticated:
        username = request.user
        
        lessons = Lesson.objects.filter(author = username)
        
    
    
    
    
    return render(request,
                  'personal/personal.html',
                  {
                   
                   'lessons': lessons})


def logout(request):
    logout(request)




def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Lesson, id = id) 
  
    # pass the object as instance in form 
    
    form = GeeksForm(request.POST or None, instance = obj) 
    
    
  
    # save the data from the form and 
    # redirect to detail_view 
    if request.user.is_authenticated:
        username = request.user
        
        if form.is_valid(): 
            form.save() 
            return render(request,'personal/return.html')
        
                
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "personal/update_view.html", context) 
def delete_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Lesson, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return render(request,'personal/return.html')
  
    return render(request, "personal/delete_view.html", context) 
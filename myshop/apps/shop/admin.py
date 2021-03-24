from django.contrib import admin
from .models import Urok, Lesson
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser

# Register your models here.
# Регистарция базы для администрирование 



class UrokAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Urok, UrokAdmin)



class LessonAdmin(admin.ModelAdmin):
   list_display = ['id','category','name','slug','upload','created','available','updated','author']
   list_filter = [ 'created', 'updated']
   list_editable = [ 'available',]
   admin.site.site_header = 'Админ панель Web Архива'
   prepopulated_fields = {'slug': ('name',)}
 
admin.site.register(Lesson, LessonAdmin)

    



        



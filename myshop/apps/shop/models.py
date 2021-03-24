from django.db import models,connection
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings




# Create your models here.
# Модели для миграции в базу данных
class Urok(models.Model):
    name = models.CharField(max_length=200, db_index=True,unique=True)
    slug = models.SlugField(max_length=210, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Урок/Сабақ'
        verbose_name_plural = 'Уроки/Сабақтар'
        

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('shop:lesson_list_by_category',
                        args=[self.slug])    



def upload_to(instance, filename):
    return 'lesson/%s/%s' % (instance.author.username, filename)




class Lesson(models.Model):
    category = models.ForeignKey(Urok, related_name='urok',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=210, db_index=True)
    author = models.ForeignKey(User,to_field="username",on_delete=models.DO_NOTHING,blank=True)
    upload = models.FileField(upload_to=upload_to)

    
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Лекция/Презентация'
        verbose_name_plural = 'Лекции/Презентации'

    
        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:lesson_detail',
                        args=[self.id, self.slug])   
   




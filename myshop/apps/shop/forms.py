from django import forms
from .models import Urok, Lesson


class GeeksForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Lesson 
  
        # specify fields to be used 
        fields = [ 
            "name", 
            "category",
            
        
        ] 
 

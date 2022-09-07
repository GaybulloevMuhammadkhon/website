from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
   class Meta:
       model = News
       fields = '__all__'




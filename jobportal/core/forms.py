from django import forms
from auth_users.models import CustomMyUser


#====================Search Form================

class SearchForm(forms.Form):
     query = forms.CharField(max_length = 100,required = False)
    

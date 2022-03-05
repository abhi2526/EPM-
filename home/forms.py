from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import*
from phonenumber_field.modelfields import PhoneNumberField
#from phone_field import PhoneField

#from django_countries.fields import CountryField

from django.contrib.auth.models import User


"""class AddEmpFOrm(forms.ModelForm):
    
    class Meta:
        model = employee
        CHOICES= ('',"select")
        fields = ['ename', 'father_name', 'Designation', 'subDept','Replacment','salery','Cnic','phone','issueDate','Address','pic','nicCopy']
        widgets ={'ename':forms.TextInput(attrs={'class':'form-control',}),
                    'father_name':forms.TextInput(attrs={'class':'form-control','required':'True'}),
                    'Designation':forms.TextInput(attrs={'class':'form-control','required':'True'}),
                    'subDeptart':forms.Select(choices=CHOICES,attrs={'class':'form-control','id':'select3','required':'True'}),
                    'Replacment':forms.Select(attrs={'class':'form-control','queryset':'employee.objects.all()','required':'True'}),
                    'salery':forms.NumberInput(attrs={'class':'form-control','required':'True'}),
                    'Cnic':forms.NumberInput(attrs={'class':'form-control','required':'True'}),
                    'phone':forms.NumberInput(attrs={'class':'form-control','required':'True'}),
                    'issueDate':forms.DateInput(attrs={'class':'form-control', 'type':'date','required':'True'}),
                    'Address':forms.Textarea(attrs={'class':'form-control','required':'True'}),
                    'nicCopy':forms.ClearableFileInput(attrs={'class':'form-control','required':'True'}),
                    'pic':forms.ClearableFileInput(attrs={'class':'form-control','required':'True'}),
   
                  
        }
        initial = {
            'Replacment': 'D'
        }

class CreateUserForm(UserCreationForm):
    phone=forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'phone']"""
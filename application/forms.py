from django import forms
from .models import ProjectCybrom


from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User   # iske through user badha rhe h




class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput({'class':'abc'}))
    password2=forms.CharField(widget=forms.PasswordInput({'class':'abc'}))
    class Meta:   #database se field le rhe h isiye Meta krte h
        model=User
        fields=['username','first_name','last_name','email']#kitni field chahiye ye uske liye all kro ya perticular name  specify kro
             
        widgets={
            'username':forms.TextInput(attrs={'class':'abc',
                                              'placeholder':'random'}),
            'first_name':forms.TextInput(attrs={'class':'abc'}),
            'last_name':forms.TextInput(attrs={'class':'abc'}),
            'email':forms.TextInput(attrs={'class':'abc'}),

             }
        
class LoginForm(AuthenticationForm):
    pass


class ShowImage(forms.ModelForm):
    class Meta:
        model=ProjectCybrom
        fields='__all__'


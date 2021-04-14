from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def clean_password2(self):
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password != password2 :
            raise forms.ValidationError("Password doesn't match!!.")

    def save(self,commit=True,*args,**kwargs):
        obj=super(UserRegisterForm,self).save(commit=False,*args,**kwargs)
        password=self.cleaned_data.get('password')  
        obj.set_password(password)
        obj.save()
        return obj


class UserLoginForm(forms.Form):
    username=forms.CharField(label="UserName", required=True)
    password=forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid Login Credentials!!. Please try again.")
        return self.cleaned_data

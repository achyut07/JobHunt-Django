from django import forms
from django.contrib import admin
from django.contrib.auth import (authenticate, get_user_model, login, logout, )
from User.models import User,Jobsearch,Company,Apply
CHOICES=[('Employeer','Employeer'),
         ('jobseeker','jobseeker')]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 1:
            user = user_qs.first()
        if not user:
            raise forms.ValidationError("This user doesn't exist.")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password.")
        if not user.is_active:
            raise forms.ValidationError("The user is no longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    Choose = forms.ChoiceField(widget=forms.RadioSelect(attrs={'placeholder': 'Choose your '}), choices=CHOICES)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password','Choose', 'Department', 'Contactnum']
    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")


class UserJobsearchform(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['job_title']



class Userjobpostform(forms.ModelForm):
    class Meta:
        model=Company
        fields= '__all__'


class Chooseform(forms.ModelForm):
    class Meta:
        model=User
        fields=['Choose']



class Applyform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Apply
        fields=['Applier_email','password','Company_email','cv']



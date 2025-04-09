from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=30, required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(label='Last Name', max_length=30, required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Last Name"}))
    username = forms.CharField(label='Username', max_length=30, required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    phone = forms.CharField(label='Phone', max_length=15, required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Phone"}))
    email = forms.EmailField(label='Email', max_length=254, required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Email"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}),
            'password2': forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Retype Password"}),
        }

    def save(self, commit=True):

        user = super().save()
        if user:
            Profile.objects.create(user=user, first_name=self.cleaned_data["first_name"], last_name=self.cleaned_data["last_name"], phone_number=self.cleaned_data["phone"])
            
        return user
from django import  forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))

# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Account
#         fields = ('email', 'name', 'phone', 'password')
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#
#         if commit:
#             user.save()
#
#         return user
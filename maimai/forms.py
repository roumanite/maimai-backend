from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # widgets = {
        #     'password': forms.PasswordInput(),
        #     'confirm_password':forms.PasswordInput(),
        # }
        fields = ('username','first_name','last_name','email','gender','birthday')
    def save(self,user):
        # profile.save()
        user.save()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # widgets = {
        #     'password': forms.PasswordInput(),
        #     'confirm_password': forms.PasswordInput(),
        # }
        fields = ('username','first_name','last_name','email','gender','birthday')

# class CustomerCreationForm(forms.ModelForm):
#     # password = forms.CharField(widget=forms.PasswordInput)
#     # confirm_password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Customer
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
#         fields = ('username','email','password')
#
# class CustomerChangeForm(forms.ModelForm):
#     # password = forms.CharField(widget=forms.PasswordInput)
#     # confirm_password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Customer
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
#         fields = ('username','email','password',)

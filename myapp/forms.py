from django import forms
from .models import Employee,Register,Group


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields="__all__"
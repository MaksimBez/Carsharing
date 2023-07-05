from django.forms import ModelForm, TextInput, Textarea
from car.models import Auto, Brand, AutoModel, User
from django import forms


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            })
        }


class CreateAutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['vin_code']

        widgets = {
            'vin_code': TextInput(attrs={
                'placeholder': 'Vin'
            })
        }


class CreateBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Brand'
            }),
        }


class CreateModelForm(forms.ModelForm):
    class Meta:
        model = AutoModel
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Model'
            })
        }

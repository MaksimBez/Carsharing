from django.forms import TextInput
from car.models import Auto, Brand, AutoModel, User
from django import forms

from car.validators import brand_validate


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


class CreateCarForm(forms.Form):
    brand_name = forms.CharField(max_length=10, validators=[brand_validate])
    model_name = forms.CharField(max_length=255)
    vin_code = forms.CharField()

    def save(self):
        brand_name = self.cleaned_data['brand_name']
        model_name = self.cleaned_data['model_name']
        vin_code = self.cleaned_data['vin_code']

        brand, _ = Brand.objects.get_or_create(name=brand_name)
        model = AutoModel.objects.create(brand=brand, name=model_name)
        Auto.objects.create(vin_code=vin_code, auto_model=model)

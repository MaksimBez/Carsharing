from django.shortcuts import render
from .models import User, Auto, AutoModel, Brand
from django.contrib import messages
from django.shortcuts import redirect
from .forms import CreateAutoForm, CreateBrandForm, CreateModelForm, CreateUserForm

def main(request):
    return render(request, 'main.html')


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created!")
            return redirect('/create_user/')
        else:
            messages.error(request, "Phone already exists")
    else:
        form = CreateUserForm()
    return render(request, 'create_user.html', {'form': form})


def create_car(request):
    if request.method == 'POST':
        auto_form = CreateAutoForm(request.POST)
        brand_form = CreateBrandForm(request.POST)
        model_form = CreateModelForm(request.POST)
        if auto_form.is_valid() and brand_form.is_valid() and model_form.is_valid():
            model_form.save()
            brand_form.save()
            auto_form.save()
            messages.success(request, "Your account has been created!")
            return redirect('/main/')
    else:
        auto_form = CreateAutoForm()
        brand_form = CreateBrandForm()
        model_form = CreateModelForm()
    return render(request, 'create_car.html', {'auto_form': auto_form, 'brand_form': brand_form, 'model_form': model_form})


def book_car(request):
    if request.method == 'GET':
        return render(request, 'book_car.html')




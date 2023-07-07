from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import CreateUserForm, CreateCarForm


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
        car_form = CreateCarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Your account has been created!")
            return redirect('/main/')
    else:
        car_form = CreateCarForm()
    return render(request, 'create_car.html', {'form': car_form})


def book_car(request):
    if request.method == 'GET':
        return render(request, 'book_car.html')




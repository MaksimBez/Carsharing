from django.urls import path
from car.views import main, create_user, create_car, book_car


urlpatterns = [
    path('main/', main),
    path('create_user/', create_user),
    path('create_car/', create_car),
    path('book_car/', book_car),
]
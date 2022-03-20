from django.shortcuts import render, redirect

from carsharing.forms import CarForm
from carsharing.models import Car


def cars(request):
    cars = Car.objects.all().order_by('brand')
    context = {
        'cars': cars
    }
    return render(request, 'carsharing/cars.html', context)


def create(request):
    error = ''
    if request.POST:
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/carsharing/')
        else:
            error= form.errors

    form = CarForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'carsharing/create_car.html', context)


def car(request, brand):
    model = request.GET.get('model', '')

    if brand == 'lada':
        return redirect('/carsharing/GG/', permanent=False)

    available_cars = [{
        'brand': 'opel',
        'model': 'astra',
        'price': 500,
    }, {
        'brand': 'vw',
        'model': 'passat',
        'price': 1000,
    }]
    context = {
        'brand': brand,
        'model': model,
        'available_cars': available_cars,
    }
    return render(request, 'carsharing/car.html', context)

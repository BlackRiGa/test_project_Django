from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect

from carsharing.forms import CarForm
from carsharing.models import Car
from django.views.generic import DeleteView, UpdateView, DetailView


class CarDetailView(DetailView):
    model = Car
    template_name = 'carsharing/car_details.html'
    context_object_name = 'car'


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'carsharing/create_car.html'
    form_class = CarForm

    def form_invalid(self, form):
        return HttpResponse("form is invalid.. this is just an HttpResponse object {}".format(form.errors))


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'carsharing/car_delete.html'
    success_url = '/carsharing/'


def cars(request):
    cars = Car.objects.all().order_by('brand')
    context = {
        'cars': cars
    }
    return render(request, 'carsharing/cars.html', context)


def create(request):
    if not request.user.is_superuser and not request.user.is_staff:
        raise PermissionDenied()
    error = ''
    if request.POST:
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/carsharing/')
        else:
            error = form.errors

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

from django.shortcuts import render, redirect

from market.forms import ProductForm
from market.models import Product


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'market/products.html', context)


def create(request):
    error = ''
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/market/')
        else:
            error = form.errors

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'market/create_mouse.html', context)
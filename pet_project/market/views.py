from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.views.generic import DeleteView, UpdateView, DetailView

from market.forms import ProductForm
from market.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'market/product_details.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'market/create_product.html'
    form_class = ProductForm

    def form_invalid(self, form):
        return HttpResponse("form is invalid.. this is just an HttpResponse object {}".format(form.errors))


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'market/product_delete.html'
    success_url = '/market/'


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'market/products.html', context)


def create(request):
    if not request.user.is_superuser and not request.user.is_staff:
        raise PermissionDenied()
    error = ''
    if request.POST:
        form = ProductForm(request.POST, request.FILES)
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
    return render(request, 'market/create_product.html', context)


def get_image(self, product):
    if product.image:
        return mark_safe(f'<img src={product.image.url} height="58" width="58">')
    return ''

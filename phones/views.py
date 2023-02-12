from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    context = {}
    if sort_by == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort_by == 'min_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone_objects = Phone.objects.filter(slug=slug)
    context = {
        'phone': phone_objects
    }
    return render(request, template, context)

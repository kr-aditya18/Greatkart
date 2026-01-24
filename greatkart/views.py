from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.filter(is_available=True).order_by('created_date')

    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)

def health_check(request):
    return HttpResponse("OK")

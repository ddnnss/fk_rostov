from django.shortcuts import render

def cart(request):
    return render(request, 'pages/cart.html', locals())

def checkout(request):
    return render(request, 'pages/checkout.html', locals())
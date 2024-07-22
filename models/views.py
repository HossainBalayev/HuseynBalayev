from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    return render(request, 'main.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def shop_details(request):
    return render(request, 'shop-details.html')

def shop(request):
    return render(request, 'shop.html')

def shopping_cart(request):
    return render(request, 'shopping-cart.html')
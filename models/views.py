from django.shortcuts import render, redirect
from .models import Product, Blog
from .forms import ContactForm

def home(request):
    context = {
        'products' : Product.objects.all(),
    }
    return render(request, 'index.html', context)

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    return render(request, 'main.html')

def blog(request):
    context = {
        'blogs' : Blog.objects.all(),
    }
    return render(request, 'blog.html', context)

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

def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog-details.html', context)



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def search_field(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none() 

    context = {
        'products': products,
    }
    return render(request, 'search.html', context=context)



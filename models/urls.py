from django.urls import path
from .views import home, base, about, main, blog_details, blog, checkout, contact, shop_details, shop, shopping_cart, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('about/', about, name='about'),
    path('main/', main, name='main'),
    path('blog/<int:id>/', blog_details, name='blog_details'),
    path('blog/', blog, name='blog'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),  
    path('shop_details/', shop_details, name='shop_details'),
    path('shop/', shop, name='shop'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('contact_view/', contact_view, name='contact'),

]






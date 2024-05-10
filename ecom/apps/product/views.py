import random

from django.contrib import messages
#from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404

from .forms import AddToCartForm
from .models import Category, Brand, Product,Size,Color

from apps.cart.cart import Cart

def product(request,category_slug, product_slug):
    cart = Cart(request)
    

    product = get_object_or_404(Product,category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            
            title_c = request.POST['color']
            new_color = Color(title=title_c)
            new_color.save()

            title = request.POST['size']

            new_size=Size(title=title)

            new_size.save()
            
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'the product is added to the cart')

            return redirect('product',category_slug=category_slug, product_slug=product_slug)
    else:
        form =  AddToCartForm()



    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product/product.html', {'form':form, 'product': product, 'similar_products': similar_products})
    

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category) #filter(parrent=none to shw)

    return render(request, 'product/category.html', {'products':products,'category': category})

def brand(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(brand=brand)

    return render(request, 'product/brand.html', {'products':products,'brand': brand})




def size_input(request):

    if request.method == 'POST':
        
        title = request.POST['size']

        new_size=Size(title=title)

        new_size.save()

    return render(request,'templates/product.html',{})
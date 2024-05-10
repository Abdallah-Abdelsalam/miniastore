from django.shortcuts import get_object_or_404, render

from apps.product.models import Product,Brand

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    #best_sellers_products = Product.objects.filter(slug__startswith='best_seller').values()
    
    return render(request, "core/frontpage.html", {'newest_products': newest_products})

def brandpage(request):
    brand= Brand.objects.all()

    return render (request,"core/brand_page.html",{'brand':brand})  

def contact(request):
    return render(request, "core/contact.html")

 
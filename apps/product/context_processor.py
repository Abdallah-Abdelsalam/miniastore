from apps.product.models import Category, Brand

def menu_categories(request):
    categories = Category.objects.all()#[9:]

    return {'menu_categories': categories}


def menu_brands(request):
    brands = Brand.objects.all()

    return {'menu_brands': brands}
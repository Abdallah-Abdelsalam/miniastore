from django.contrib import admin

from .models import Category, Product, Brand, ProductImage,Color,Size,ProductAttribute

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ProductImage)
admin.site.register(Size)

class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)
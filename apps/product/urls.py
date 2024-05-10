from django.urls import path

from . import views

from apps.core.views import frontpage

urlpatterns = [
    path('', frontpage,name='frontpage'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:brand_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category'),
    path('<slug:brand_slug>/', views.brand, name='brand')

] 

#path('category-list',views.category_list,name='category-list'),
   # path('brand-list',views.brand_list,name='brand-list'),
 #   path('product-list',views.product_list,name='product-list'),
  #  path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    
   # path('product/<str:slug>/<int:id>',views.product_detail,name='product_detail'),

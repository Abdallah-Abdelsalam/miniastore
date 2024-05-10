from django.forms import ModelForm
from apps.product.models import Product

class  ProductForm(ModelForm):
    class Meta:
        model = Product
        fields =  ['category', 'brand','image' , 'title', 'description' ,'price']
    
#    def save(self, commit=True):
 #           product = super().save(commit=False)
  #          if commit:
   #             if self.cleaned_data['image']:
    #                product.image = self.cleaned_data['image']
     #           product.save()
      #      return product
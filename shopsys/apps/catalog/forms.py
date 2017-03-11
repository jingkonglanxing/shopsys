from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean_price(self):   ##检验 价格  必须大于0
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0.')
        return self.cleaned_data['price']
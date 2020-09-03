from django import forms
PRODUCT_QUANTITY_SHOICES = [(i, str(i)) for i in range(1,21)]

class CardAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(shoices=PRODUCT_QUANTITY_SHOICES, coerce=int)
    update = forms.BooleanField(request=False, initial=False, widget=forms.hiddenInput)



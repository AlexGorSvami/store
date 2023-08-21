from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'address')

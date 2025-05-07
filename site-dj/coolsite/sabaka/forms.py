from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Flower, Supplier, Delivery, Review, Promotion, Category, Order

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'description', 'price', 'photo', 'is_available', 'category']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_email', 'phone', 'address']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['name', 'cost', 'estimated_time']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['flower', 'customer_name', 'rating', 'comment']

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'discount', 'start_date', 'end_date', 'banner']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, label='Количество')
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_method', 'address']
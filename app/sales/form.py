from django import forms
from datetime import datetime
from .models import Item, Customer, Seller


class CustomerForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=30)
    lastname = forms.CharField(label="Фамилия", max_length=30)
    phone = forms.RegexField(label="Контактный телефон", regex=r'^\+?7?\d{10}$')
    email = forms.EmailField(label="Email")


class SellerForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=30)
    lastname = forms.CharField(label="Фамилия", max_length=30)
    phone = forms.CharField(label="Контактный телефон", max_length=10)
    email = forms.EmailField(label="Email")
    date_admission = forms.DateField(label="Дата приема на работу", required=datetime.now())
    post = forms.ChoiceField(label="Позиция в фирме", choices=(('seller', 'Продавец'),
                                                               ('older_seller', 'Старший продавец'),
                                                               ('head_sales_department', 'Руководитель отдела продаж')))


class ItemForm(forms.Form):
    name = forms.CharField(label="Название товара", max_length=30)
    info = forms.CharField(label="Описание товара", widget=forms.Textarea)


class OrderForm(forms.Form):
    date = forms.DateField(label="Дата продажи", required=datetime.now())
    total = forms.IntegerField(label="Сумма продажи")
    customer = forms.ChoiceField(label="Покупатель", choices=[Customer.objects.all()])
    seller = forms.ChoiceField(label="Продавец", choices=[Seller.objects.all()])


class PositionsForm(forms.Form):
    item = forms.ChoiceField(label="Товар", choices=[Item.objects.all()])
    order = forms.ChoiceField(label="Продажа", choices=[OrderForm.objects.all()])
from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+?7?\d{10}$')], max_length=12, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Posts(models.TextChoices):
    seller = 'Продавец'
    older_seller = 'Старший продавец'
    head_sales_department = 'Руководитель отдела продаж'


class Seller(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+?7?\d{10}$')], max_length=12, blank=True)
    email = models.EmailField(blank=True)
    date_admission = models.DateField(auto_now=True)
    post = models.TextField(choices=Posts)

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Item(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    date = models.DateField(auto_now=True)
    total = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class Positions(models.Model):
    item = models.ManyToManyField(Item)
    order = models.ManyToManyField(Order)
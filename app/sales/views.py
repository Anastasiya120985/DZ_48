from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .form import ItemForm, CustomerForm, SellerForm
from .models import Item, Customer, Seller


def index(request):
    template = loader.get_template("index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))


def get_context(title, d=None):
    context = {'title': title,
               'pages': [('item/', 'Товары'),
                         ('customer/', 'Покупатель'),
                         ('seller/', 'Продавец')]
                         }
    if d:
        for k in d:
            context[k] = d[k]
    return context


def item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        info = request.POST.get("info")
        u = {'name': name, 'info': info}
        content = get_context('Товар', u)
        u = Item(name=name, info=info)
        u.save()
    else:
        userform = ItemForm()
        content = get_context('Товар', {"form": userform})
    return render(request, "item.html", content)


def customer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        u = {'name': name, 'lastname': lastname, 'phone': phone, 'email': email}
        content = get_context('Покупатель', u)
        u = Customer(name=name, lastname=lastname, phone=phone, email=email)
        u.save()
    else:
        userform = CustomerForm()
        content = get_context('Покупатель', {"form": userform})
    return render(request, "customer.html", content)


def seller(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        date_admission = request.POST.get("date_admission")
        post = request.POST.get("post")
        u = {'name': name, 'lastname': lastname, 'phone': phone, 'email': email, 'date_admission': date_admission, 'post': post}
        content = get_context('Продавец', u)
        u = Seller(name=name, lastname=lastname, phone=phone, email=email, date_admission=date_admission, post=post)
        u.save()
    else:
        userform = SellerForm()
        content = get_context('Продавец', {"form": userform})
    return render(request, "seller.html", content)
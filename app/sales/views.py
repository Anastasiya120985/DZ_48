from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template("index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))


def get_context(title, d=None):
    context = {'title': title,
               'pages': [('football/', 'Футбол'),]
                         }
    if d:
        for k in d:
            context[k] = d[k]
    return context
from django.shortcuts import render

from .renter_list import renter
from .ts_list import ts
from .refer_list import refer


# Главная страница
def index(request):    
    template = 'index.html'
    renter_list = renter()
    ts_list = ts()
    refer_list = refer()
    context = {
        'renter_list': renter_list,
        'ts_list': ts_list,
        'refer_list': refer_list,
    }
    return render(request, template, context)

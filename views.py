from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def cart(request):
    val1 = request.GET['list']
    val2 = request.GET['search']
    val3 = request.POST['add']
    val4 = request.DELETE['remove']

    shipment = val1+val2+val3+val4

    return render(request, "order.html", {'order': shipment})
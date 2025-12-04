from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }
    return render(request, "myapp/index.html", context)

def detail(request, id):
    return HttpResponse(f'this is a detail view for item with id: {id}')

def item(request):
    return HttpResponse("this is an item view")
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.
def index(request):
    list_of_items = Item.objects.all()
    context = {
        'list_of_items': list_of_items,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("This is an item view")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
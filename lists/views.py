from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List

def home_page(request):
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-new-page/')
    
    # items = Item.objects.all()
    # return render(request, 'home.html',{'items':items})
    return render(request, 'home.html')
# Create your views here.

def view_list(request,list_id):
    list_user = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_user)
    return render(request, 'list.html',{'items':items})


def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_user)
    return redirect(f'/lists/{list_user.id}/')


def add_item(request,list_id):
    list_user = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_user)
    return redirect(f'/lists/{list_user.id}/')
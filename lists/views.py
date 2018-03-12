from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item


def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']  # item_text 必须是表单中input框中的name值， 获取前端提交的数据
    #     Item.objects.create(text=new_item_text)
    #     return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    contexts = {'items': items}
    return render(request, 'list.html', contexts)


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

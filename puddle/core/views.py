from django.shortcuts import render, redirect
from item.models import Item, Category
from core.form import SignUp


def index(request):
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories':categories,
        'items': items
    })  


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method =='POST':
        form = SignUp(request.POST)

        if form.is_valid():
             form.save()
             return redirect('/login')
    else:        
        form = SignUp()

    return render(request, 'core/signup.html', {
    'form':form})
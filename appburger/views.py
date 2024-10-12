from django.shortcuts import render, get_object_or_404, redirect
from market.models import BurgerList, Order
from django.contrib.auth.decorators import login_required
from market.forms import OrderForm

def Home(requests):
    return render(requests, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Market(request):
    data = BurgerList.objects.all()
    return render(request, 'market.html', {'data': data})

def burger_detail(request, pk):
    burger = get_object_or_404(BurgerList, pk=pk)
    return render(request, 'products.html', {'burger': burger})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section':'dashboard'})



def submit_order(request, pk):
    burger = BurgerList.objects.get(id=pk)  # ბურგერის ინფორმაციის მოპოვება
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)  # შეკვეთას ქმნით, მაგრამ ჯერ არ ვახორციელებთ
            order.burger = burger  # ბურგერის დასმა შეკვეთაში
            order.save()  # შენახვა
            return redirect('order_success')  # წარმატების გვერდზე გადამისამართება
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form, 'burger': burger})



def order_success(request):
    return render(request, 'submit_order.html')


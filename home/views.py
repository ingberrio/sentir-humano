from django.shortcuts import render
from suppliers.models import Supplier

def home(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, 'home.html', context)

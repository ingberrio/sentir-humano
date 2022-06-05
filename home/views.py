from django.shortcuts import render
from suppliers.models import Supplier
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q 

def home(request):
    suppliers = Supplier.objects.all()
    
    # Search suppliers home
    
    search_supplier = request.GET.get('search') # Get url parameter from a form submitting from home
    search_city = request.GET.get('city')
    search_specialty = request.GET.get('specialty')

    if search_supplier:
        suppliers = Supplier.objects.filter(Q(specialty__icontains=search_supplier) 
                                          | Q(first_name__icontains=search_supplier)
                                          | Q(city__icontains=search_supplier))
    elif search_city:
        suppliers = Supplier.objects.filter(Q(specialty__icontains=search_city) 
                                          | Q(first_name__icontains=search_city)
                                          | Q(city__icontains=search_city))
    elif search_specialty:
        suppliers = Supplier.objects.filter(Q(specialty__icontains=search_specialty) 
                                          | Q(first_name__icontains=search_specialty)
                                          | Q(city__icontains=search_specialty))
    else:
        suppliers = Supplier.objects.all()  # If not searched, return default suppliers

    number_suppliers = Supplier.objects.filter().count() # Get numbers of suppliers
    
    # Pagination 
    
    page_num = request.GET.get('page', 1)
    paginator = Paginator(suppliers, 6) # 6 supplier per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'suppliers': suppliers,
        'page_obj': page_obj,
        'number_suppliers': number_suppliers,
    }
    return render(request, 'home.html', context)

from django.shortcuts import render
from suppliers.models import Supplier
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q 

def home(request):
    suppliers = Supplier.objects.all()
    
    # Search field home
    
    search_post = request.GET.get('search') # Get url parameter from a form submitting from a web page
    if search_post:
        suppliers = Supplier.objects.filter(Q(specialty__icontains=search_post) 
                                          | Q(first_name__icontains=search_post)
                                          | Q(city__icontains=search_post))
    else:
        # If not searched, return default posts
        suppliers = Supplier.objects.all()

    number_suppliers = Supplier.objects.filter().count() # Numbers of suppliers
    
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
        'search_post': search_post,
    }
    return render(request, 'home.html', context)

from django.shortcuts import render
from suppliers.models import Supplier
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    suppliers = Supplier.objects.all()
    number_suppliers = Supplier.objects.filter().count()
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

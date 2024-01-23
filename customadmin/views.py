from django.core import serializers
from django.http import JsonResponse 
from typing import Any
from django.views.generic.base import TemplateView
from django.shortcuts import render
from customadmin.models import Customer
import math
from django.db.models import Q

# Create your views here.
def dashboard(request):
    return render(request, "customadmin/dashboard.html")

class CustomersList(TemplateView):
    template_name = "customadmin/customers.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        context['count'] = Customer.objects.count()
        # context['count'] = (customer_count := Customer.objects.count())
        # context['pages'] = range(1,math.ceil(customer_count/5)+1)
        return context

def customerListApi(request):
    search = request.GET.get('search')
    limit = int(request.GET.get('show', 5))
    page = int(request.GET.get('page', 1))
    offset = limit*(page-1)
    query_set = Customer.objects.order_by('-created_at')
    count = None
    if search:
        query_set = query_set.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)
        )
        count = query_set.count()
    data = query_set.values()[offset:offset+limit]
    return JsonResponse({
        'customers': list(data),
        'count': count
    }, safe=False)
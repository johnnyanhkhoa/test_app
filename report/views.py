from django.shortcuts import render,redirect
from datetime import datetime
from django.core.paginator import Paginator
from sale_management.models import *
from quotation.models import *

# Create your views here.
def report_contract(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Đọc danh sách contract theo status
    if pk == 0:
        contracts = Contract.objects.order_by('contract_no')
    else:
        contracts = Contract.objects.filter(contract_status=pk).order_by('contract_no')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(contracts, 15)
    contract_pager = paginator.page(page)
    
    return render(request, 'report/report_contract.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'contracts' : contract_pager,
    })
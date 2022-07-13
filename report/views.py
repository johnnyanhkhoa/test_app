from django.shortcuts import render,redirect
from datetime import datetime
from django.core.paginator import Paginator
from sale_management.models import *
from quotation.models import *
from report.forms import *

# Create your views here.
def report_contract(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Đọc danh sách all contract theo channel
    if pk == 0:
        contracts = Contract.objects.filter(contract_status=None).order_by('contract_no')
    else:
        contracts = Contract.objects.filter(channel=pk).order_by('contract_no')
        # print(contracts.contract_status)

    # Phân trang all contract
    page = request.GET.get('page', 1)
    paginator = Paginator(contracts, 15)
    contract_pager = paginator.page(page)
            
    # Đọc danh sách "đã chuyển khách hàng" contract
    contracts_da_chuyen_khach_hang = Contract.objects.filter(contract_status=1).order_by('contract_no')

    # Phân trang "đã chuyển khách hàng" contract
    page = request.GET.get('page', 1)
    paginator = Paginator(contracts_da_chuyen_khach_hang, 15)
    contracts_da_chuyen_khach_hang_pager = paginator.page(page)
    
    # Đọc danh sách "đã ký" contract
    contracts_da_ky = Contract.objects.filter(contract_status=2).order_by('contract_no')

    # Phân trang "đã ký" contract
    page = request.GET.get('page', 1)
    paginator = Paginator(contracts_da_ky, 15)
    contracts_da_ky_pager = paginator.page(page)
    
    # Đọc danh sách "hủy" contract
    contracts_huy = Contract.objects.filter(contract_status=3).order_by('contract_no')

    # Phân trang "hủy" contract
    page = request.GET.get('page', 1)
    paginator = Paginator(contracts_huy, 15)
    contracts_huy_pager = paginator.page(page)
    
    return render(request, 'report/report_contract.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'contracts' : contract_pager,
        'contracts_da_chuyen_khach_hang' : contracts_da_chuyen_khach_hang_pager,
        'contracts_da_ky' : contracts_da_ky_pager,
        'contracts_huy' : contracts_huy_pager,
    })


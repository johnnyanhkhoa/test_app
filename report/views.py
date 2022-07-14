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

def contract_follow_up(request, pk):
    # Contract
    contract = Contract.objects.get(pk=pk)
    
    # Contract follow up
    form_follow_up = ContractFollowupForm(instance=contract)
    if request.method == 'POST':
        form_follow_up = ContractFollowupForm(request.POST, instance=contract)
        if form_follow_up.is_valid():
            form_follow_up.save()
            return redirect('/report_contract/0/')
    
    return render(request, 'report/form_contract_follow_up.html', {
        'contract' : contract,
        'form_follow_up' : form_follow_up,
    })

def report_quotation(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Đọc danh sách all quotation theo channel
    if pk == 0:
        quotations = Quotation.objects.filter(quotation_status=None).order_by('quotation_no')
    else:
        quotations = Quotation.objects.filter(channel=pk).order_by('quotation_no')

    # Phân trang all quotation
    page = request.GET.get('page', 1)
    paginator = Paginator(quotations, 15)
    quotation_pager = paginator.page(page)
            
    # Đọc danh sách "đã chuyển khách hàng" quotation
    quotations_da_chuyen_khach_hang = Quotation.objects.filter(quotation_status=1).order_by('quotation_no')

    # Phân trang "đã chuyển khách hàng" quotation
    page = request.GET.get('page', 1)
    paginator = Paginator(quotations_da_chuyen_khach_hang, 15)
    quotations_da_chuyen_khach_hang_pager = paginator.page(page)
    
    # Đọc danh sách "đã ký" quotation
    quotations_da_ky = Quotation.objects.filter(quotation_status=2).order_by('quotation_no')

    # Phân trang "đã ký" quotation
    page = request.GET.get('page', 1)
    paginator = Paginator(quotations_da_ky, 15)
    quotations_da_ky_pager = paginator.page(page)
    
    # Đọc danh sách "hủy" quotation
    quotations_huy = Quotation.objects.filter(quotation_status=3).order_by('quotation_no')

    # Phân trang "hủy" quotation
    page = request.GET.get('page', 1)
    paginator = Paginator(quotations_huy, 15)
    quotations_huy_pager = paginator.page(page)
    
    return render(request, 'report/report_quotation.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'quotations' : quotation_pager,
        'quotations_da_chuyen_khach_hang' : quotations_da_chuyen_khach_hang_pager,
        'quotations_da_ky' : quotations_da_ky_pager,
        'quotations_huy' : quotations_huy_pager,
    })

def quotation_follow_up(request, pk):
    # Quotation
    quotation = Quotation.objects.get(pk=pk)
    
    # Edit customer
    form_follow_up = QuotationFollowupForm(instance=quotation)
    if request.method == 'POST':
        form_follow_up = QuotationFollowupForm(request.POST, instance=quotation)
        if form_follow_up.is_valid():
            form_follow_up.save()
            return redirect('/report_quotation/0/')
    
    return render(request, 'report/form_quotation_follow_up.html', {
        'quotation' : quotation,
        'form_follow_up' : form_follow_up,
    })
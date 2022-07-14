from urllib import response
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.template.loader import render_to_string
from datetime import datetime
import pdfkit
from django.core.paginator import Paginator
import quotation
from .models import *
from .forms import *


# Create your views here.

# QUOTATION
def quotation_list_status(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')

    # Create quotation
    form = CreateQuotationForm()
    if request.method == 'POST':
        form = CreateQuotationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quotation-list-status/0/')
        
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Đọc danh sách sản phẩm theo status
    if pk == 0:
        quotations = Quotation.objects.order_by('quotation_no')
    else:
        quotations = Quotation.objects.filter(quotation_status=pk).order_by('quotation_no')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(quotations, 15)
    quotation_pager = paginator.page(page)
    
    return render(request, 'quotation/quotation_list.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'quotations' : quotation_pager,
        'customers' : customers,
        'form' : form,
    })


def quotation_delete(request, pk):
    try:
        quotation_info = Quotation.objects.get(id = pk)
    except Quotation.DoesNotExist:
        return redirect('index')
    quotation_info.delete()
    return redirect('/quotation-list-channel/0/')
    
    
def quotation_list_channel(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Create quotation
    form = CreateQuotationForm()
    if request.method == 'POST':
        form = CreateQuotationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quotation-list-channel/0/')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Đọc danh sách sản phẩm theo Channel
    quotations = Quotation.objects.all()
    if pk == 0:
        quotations = Quotation.objects.order_by('quotation_no')
    else:
        customer_name = Customer.objects.get(customer_name=quotations.customer_id)
        channel = customer_name.channel
        quotations = Quotation.objects.filter(channel=pk).order_by('quotation_no')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(quotations, 15)
    quotation_pager = paginator.page(page)

    
    return render(request, 'quotation/quotation_list.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'quotations' : quotation_pager,
        'customers' : customers,
        'form' : form,
    })
    

def quotation_update(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Edit quotation
    quotation = Quotation.objects.get(pk=pk)
    form_update_quotation = CreateQuotationForm(instance=quotation)
    if request.method == 'POST':
        form_update_quotation = CreateQuotationForm(request.POST, instance=quotation)
        if form_update_quotation.is_valid():
            form_update_quotation.save()
            return redirect('/quotation-list-channel/0/')
    return render(request, 'quotation/form_update_quotation.html', {
        'quotation' : quotation,
        'form_update_quotation' : form_update_quotation,
    })


def quotation_product_input(request, pk):
    # Quotation
    quotation = Quotation.objects.get(pk=pk)
    customer_name = Customer.objects.get(customer_name=quotation.customer_id)
    channel = customer_name.channel
    
    # Add product to quotation
    add_product_to_quotation_success_aleart = ''
    products = Product.objects.all()
    channels = Channel.objects.all()
    unit_price_vat = 1
    
    if request.POST.get('btn_addproducttoquotation'):
        quotation_name = request.POST.get('quotation_id') # lấy từ <input type="hidden">
        quotation_id = Quotation.objects.only('id').get(id=quotation_name)
        product_id = request.POST.get('product_id')  
        product_name = Product.objects.only('id').get(id=product_id)
        product = Product.objects.get(id=product_id)
        if str(channel) == 'ETC':
            unit_price_vat = product.selling_price_etc_vat
        if str(channel) == 'OTC':
            unit_price_vat = product.selling_price_otc_vat
        add_product_to_quotation_success_aleart = '''
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                Đã đăng ký thông tin thành công.
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        '''
        quotation_product_info = Quotation_product(quotation_id=quotation_id, product_id=product_name, unit_price_vat=unit_price_vat,
                                                    )
        quotation_product_info.save()
        return redirect('/quotation-list-channel/0/')
    
    return render(request, 'quotation/form_add_product_to_quotation.html', {
        'add_product_to_quotation_success_aleart' : add_product_to_quotation_success_aleart,
        'channels' : channels,
        'products' : products,
        'quotation' : quotation,
    })
    

def search_quotation(request):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Tìm kiếm
    quotations = []
    keyword = ''
    if request.GET.get('quotation_no'):
        keyword = request.GET.get('quotation_no')
        quotations = Quotation.objects.filter(quotation_no__contains=keyword).order_by('quotation_no')
        
        # Phân trang
        page = request.GET.get('page', 1)
        paginator = Paginator(quotations, 15)
        quotation_pager = paginator.page(page)
    

    return render(request, 'quotation/quotation_list.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'quotations' : quotation_pager,
    })

    
def quotation_product_delete(request, pk):
    try:
        quotation_product_info = Quotation_product.objects.get(id = pk)
    except Product.DoesNotExist:
        return redirect('index')
    quotation_product_info.delete()
    return redirect('/quotation-list-channel/0/')
    

def final_quotation(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')

    # Lấy thông tin QUOTATION và QUOTATION PRODUCT
    quotation = Quotation.objects.get(pk=pk) 
    quotation_products = Quotation_product.objects.filter(quotation_id=pk)
    # for product in quotation_products:
    #     print(product.quantity)
    
    return render(request, 'quotation/quotation.html', {
        'quotation' : quotation,
        'quotation_products' : quotation_products,  
    })




def html_to_pdf_view(request, pk):
    today = datetime.now().strftime('%d-%m-%Y')

    # Lấy thông tin QUOTATION và QUOTATION PRODUCT
    quotation = Quotation.objects.get(pk=pk) 
    quotation_products = Quotation_product.objects.filter(quotation_id=pk)

    html_string = render_to_string('quotation/final_quotation.html', {
        'today': today,
        'quotation': quotation,
        'quotation_products': quotation_products,
    })
   
    # template = get_template('quotation/final_quotation.html')
    # html = template.render({
    #     'today': today,
    #     'quotation': quotation,
    #     'quotation_products': quotation_products,
    # })
    
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        # 'orientation': 'Landscape'
    }
    
        
    # result = BytesIO()
    
    # pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result) 
    
    config_path = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=config_path)
    
    filename = 'report_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.pdf'
    # pdfkit.from_string(html_string, os.path.join(os.path.expanduser('~'), 'Documents', filename), configuration=config)
    pdfkit.from_string(html_string, "E:\\" + filename, configuration=config, options=options)
    # if not pdf.err:
        # return HttpResponse(result.getvalue(), content_type='application/pdf')

    return HttpResponse(html_string)
    


# SALE AND PURCHASE CONTRACT
def contract(request):
    
    return render(request, 'quotation/contract_1.html')


def contract_list_status(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')

    # Create quotation
    form_create_contract = CreateContractForm()
    if request.method == 'POST':
        form_create_contract = CreateContractForm(request.POST)
        if form_create_contract.is_valid():
            form_create_contract.save()
            return redirect('/contract-list-status/0/')
        
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Đọc danh sách sản phẩm theo status
    if pk == 0:
        contracts = Contract.objects.order_by('contract_no')
    else:
        contracts = Contract.objects.filter(contract_status=pk).order_by('contract_no')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(contracts, 15)
    contract_pager = paginator.page(page)
    
    return render(request, 'quotation/contract_list.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'contracts' : contract_pager,
        'channels' : channels,
        'customers' : customers,
        'statuses' : statuses,
        'form_create_contract' : form_create_contract,
    })
    

def contract_list_channel(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')

    # Create quotation
    form_create_contract = CreateContractForm()
    if request.method == 'POST':
        form_create_contract = CreateContractForm(request.POST)
        if form_create_contract.is_valid():
            form_create_contract.save()
            return redirect('/contract-list-status/0/')
        
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    # Đọc danh sách sản phẩm theo status
    if pk == 0:
        contracts = Contract.objects.order_by('-created_at')
    else:
        contracts = Contract.objects.filter(channel=pk).order_by('-created_at')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(contracts, 15)
    contract_pager = paginator.page(page)
    
    return render(request, 'quotation/contract_list.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'contracts' : contract_pager,
        'form_create_contract' : form_create_contract,
        'channels' : channels,
        'customers' : customers,
        'statuses' : statuses,
    })


def contract_update(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Edit contract
    contract = Contract.objects.get(pk=pk)
    form_update_contract = CreateContractForm(instance=contract)
    if request.method == 'POST':
        form_update_contract = CreateContractForm(request.POST, instance=contract)
        if form_update_contract.is_valid():
            form_update_contract.save()
            return redirect('/contract-list-channel/0/')
    return render(request, 'quotation/form_update_contract.html', {
        'contract' : contract,
        'form_update_contract' : form_update_contract,
    })
    
    
def search_contract(request):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    
    # Đọc danh sách Status
    list_status = Status.objects.order_by('status')
    
    
    
    # Tìm kiếm
    contracts = []
    keyword = ''
    if request.GET.get('contract_no'):
        keyword = request.GET.get('contract_no')
        contracts = Contract.objects.filter(contract_no=keyword).order_by('-created_at')
        
        # Phân trang
        page = request.GET.get('page', 1)
        paginator = Paginator(contracts, 15)
        contract_pager = paginator.page(page)
    

    return render(request, 'quotation/contract_list.html', {
        'list_channel' : list_channel,
        'list_status' : list_status,
        'contracts' : contract_pager,
    })
    

def contract_delete(request, pk):
    try:
        contract_info = Contract.objects.get(id = pk)
    except Contract.DoesNotExist:
        return redirect('index')
    contract_info.delete()
    return redirect('/contract-list-channel/0/')


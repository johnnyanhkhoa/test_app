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
    if pk == 0:
        quotations = Quotation.objects.order_by('quotation_no')
    else:
        quotations = Quotation.objects.filter(channel_id=pk).order_by('quotation_no')

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
    

def quotation_follow_up(request, pk):
    # Quotation
    quotation = Quotation.objects.get(pk=pk)
    
    # Edit customer
    form_follow_up = QuotationFollowupForm(instance=quotation)
    if request.method == 'POST':
        form_follow_up = QuotationFollowupForm(request.POST, instance=quotation)
        if form_follow_up.is_valid():
            form_follow_up.save()
            return redirect('/quotation-list-channel/0/')
    
    return render(request, 'quotation/form_quotation_follow_up.html', {
        'quotation' : quotation,
        'form_follow_up' : form_follow_up,
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

    # Tạo Contract mới
    chuoi_kq_input_contract = ''
    channels = Channel.objects.all() # lấy channel từ customer để filter
    customers = Customer.objects.all()
    statuses = Status.objects.all()
    if request.POST.get('btncontractinput'):
        customer_name = request.POST.get('customer_name')
        customer_id = Customer.objects.only('id').get(id=customer_name)
        channel = Channel.objects.only('channel_name').get(channel_name=customer_id.channel)
        status_name = request.POST.get('status_name')
        contract_status = Status.objects.only('id').get(id=status_name)
        contract_no = request.POST.get('contract_no')
        contract_date = request.POST.get('contract_date')
        valid_from_date = request.POST.get('valid_from_date')
        valid_to_date = request.POST.get('valid_to_date')
        placement_time_in_prior_to_delivery = request.POST.get('placement_time_in_prior_to_delivery')
        delivery_time = request.POST.get('delivery_time')
        registration_document = request.POST.get('registration_document')
        payment_method = request.POST.get('payment_method')
        payment_due = request.POST.get('payment_due')
        penalty_rate_for_late_payment = request.POST.get('penalty_rate_for_late_payment')
        bank_charges_related_to_payment = request.POST.get('bank_charges_related_to_payment')
        delivery_point = request.POST.get('delivery_point')
        enquiry_for_goods_receipt = request.POST.get('enquiry_for_goods_receipt')
        enquiry_for_goods_return = request.POST.get('enquiry_for_goods_return')
        documents_to_be_delivered_with_each_delivery = request.POST.get('documents_to_be_delivered_with_each_delivery')
        complaint_time_due_to_product_issue = request.POST.get('complaint_time_due_to_product_issue')
        compensation_time = request.POST.get('compensation_time')
        support_fee_on_target_achivement = request.POST.get('support_fee_on_target_achivement')
        support_fee_on_transportation = request.POST.get('support_fee_on_transportation')
        support_fee_for_payment_due_date = request.POST.get('support_fee_for_payment_due_date')
        support_fee_for_new_pos = request.POST.get('support_fee_for_new_pos')
        support_fee_for_display = request.POST.get('support_fee_for_display')
        support_fee_for_listing = request.POST.get('support_fee_for_listing')
        support_fee_for_advertising_and_birthday = request.POST.get('support_fee_for_advertising_and_birthday')
        support_fee_for_product_creation = request.POST.get('support_fee_for_product_creation')
        method_of_support_fee_payment = request.POST.get('method_of_support_fee_payment')
        penalty_for_agreement_breach = request.POST.get('penalty_for_agreement_breach')
        chuoi_kq_input_contract = '''
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                Đã đăng ký thông tin thành công.
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        '''
        contract_info = Contract(customer_id=customer_id, channel=channel , contract_no=contract_no, contract_date=contract_date,
                               valid_from_date=valid_from_date, valid_to_date=valid_to_date, contract_status=contract_status,
                               placement_time_in_prior_to_delivery=placement_time_in_prior_to_delivery, delivery_time=delivery_time, registration_document=registration_document,
                               payment_method=payment_method, payment_due=payment_due, penalty_rate_for_late_payment=penalty_rate_for_late_payment,
                               bank_charges_related_to_payment=bank_charges_related_to_payment, delivery_point=delivery_point, enquiry_for_goods_receipt=enquiry_for_goods_receipt,
                               enquiry_for_goods_return=enquiry_for_goods_return, documents_to_be_delivered_with_each_delivery=documents_to_be_delivered_with_each_delivery, complaint_time_due_to_product_issue=complaint_time_due_to_product_issue,
                               compensation_time=compensation_time, support_fee_on_target_achivement=support_fee_on_target_achivement, support_fee_on_transportation=support_fee_on_transportation,
                               support_fee_for_payment_due_date=support_fee_for_payment_due_date, support_fee_for_new_pos=support_fee_for_new_pos, support_fee_for_display=support_fee_for_display,
                               support_fee_for_listing=support_fee_for_listing, support_fee_for_advertising_and_birthday=support_fee_for_advertising_and_birthday, support_fee_for_product_creation=support_fee_for_product_creation,
                               method_of_support_fee_payment=method_of_support_fee_payment, penalty_for_agreement_breach=penalty_for_agreement_breach)
        contract_info.save()
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
        'chuoi_kq_input_contract' : chuoi_kq_input_contract,
        'channels' : channels,
        'customers' : customers,
        'statuses' : statuses,
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
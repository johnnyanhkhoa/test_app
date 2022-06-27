from email.mime import message
from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import render, redirect
from sale_management.models import *
from .forms import *
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def product_update(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Edit customer
    product = Product.objects.get(pk=pk)
    form_update_product = CreateProductForm(instance=product)
    if request.method == 'POST':
        form_update_product = CreateProductForm(request.POST, instance=product)
        if form_update_product.is_valid():
            form_update_product.save()
            return redirect('/product1/0/')
    return render(request, 'sale_agreement/form_update_product.html', {
        'product' : product,
        'form_update_product' : form_update_product,
    })

    
def product_delete(request, pk):
    try:
        product_info = Product.objects.get(id = pk)
    except Product.DoesNotExist:
        return redirect('index')
    product_info.delete()
    return redirect('/product1/0/')
    
    
def customer_update(request, pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Edit customer
    customer = Customer.objects.get(id=pk)
    form = CreateCustomerForm(instance=customer)
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/customer_channel_filter/0/')
        
    return render(request, 'sale_agreement/form_update_customer.html', {
        'form' : form,
        
    })

def customer_detail(request,pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    # Đọc danh sách Type
    list_type = Customer_type.objects.order_by('customer_type_abbrev')
    # Đọc danh sách Sale area
    list_sale_area = Sale_area.objects.order_by('sale_area_code')
    # Đọc danh sách Province
    list_province = Province.objects.order_by('province_code')
    
    # Product detail
    customer = Customer.objects.get(pk=pk)
    
    return render(request, 'sale_agreement/customer_detail.html', {
        'list_channel' : list_channel,
        'list_type' : list_type,
        'list_sale_area' : list_sale_area,
        'list_province' : list_province,
        'customer': customer,
        
    })

def customer_delete(request, pk):
    try:
        customer_info = Customer.objects.get(id = pk)
    except Product.DoesNotExist:
        return redirect('index')
    customer_info.delete()
    return redirect('/customer_channel_filter/0/')


def product1(request, pk):
        # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Product_category
    list_category = Product_category.objects.order_by('product_category_name')
    
    # Đọc danh sách Product_brand
    list_brand = Product_brand.objects.order_by('product_brand_name')
    
    # Đọc danh sách sản phẩm theo Product_category
    if pk == 0:
        products = Product.objects.order_by('-created_at')
    else:
        products = Product.objects.filter(product_category=pk).order_by('-created_at')
        
    # Create product
    form_create_customer = CreateProductForm()
    if request.method == 'POST':
        form_create_customer = CreateProductForm(request.POST)
        if form_create_customer.is_valid():
            form_create_customer.save()
            return redirect('/product1/0/')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 15)
    products_pager = paginator.page(page)
  
    return render(request, 'sale_agreement/product.html', {
        'list_category' : list_category,
        'list_brand' : list_brand,
        'form_create_customer' : form_create_customer,
        'products': products_pager,
    })


def product2(request, pk):
        # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Product_category
    list_category = Product_category.objects.order_by('product_category_name')
    
    # Đọc danh sách Product_brand
    list_brand = Product_brand.objects.order_by('product_brand_name')
    
    # Đọc danh sách sản phẩm theo Product_category
    if pk == 0:
        products = Product.objects.order_by('-created_at')
    else:
        products = Product.objects.filter(product_brand=pk).order_by('-created_at')
        
    # Create product
    form_create_customer = CreateProductForm()
    if request.method == 'POST':
        form_create_customer = CreateProductForm(request.POST)
        if form_create_customer.is_valid():
            form_create_customer.save()
            return redirect('/product2/0/')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 15)
    products_pager = paginator.page(page)
  
    return render(request, 'sale_agreement/product.html', {
        'list_category' : list_category,
        'list_brand' : list_brand,
        'form_create_customer' : form_create_customer,
        'products': products_pager,
    })
    

def search_product(request):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Product_category
    list_category = Product_category.objects.order_by('product_category_name')
    
    # Đọc danh sách Product_brand
    list_brand = Product_brand.objects.order_by('product_brand_name')
    
    # Create product
    form_create_customer = CreateProductForm()
    if request.method == 'POST':
        form_create_customer = CreateProductForm(request.POST)
        if form_create_customer.is_valid():
            form_create_customer.save()
            return redirect('/product2/0/')
    
    # Tìm kiếm
    products = []
    keyword = ''
    result_search = ''
    if request.GET.get('product_name'):
        keyword = request.GET.get('product_name')
        products = Product.objects.filter(product_name__contains=keyword).order_by('-created_at')
        
        # Phân trang
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 15)
        products_pager = paginator.page(page)
    

    return render(request, 'sale_agreement/product.html', {
        'list_category' : list_category,
        'list_brand' : list_brand,
        'products': products_pager,
        'form_create_customer' : form_create_customer,
        'category_name': result_search,
        'product_name': keyword,
    })
    

def product_detail(request,pk):
    # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Product_category
    list_category = Product_category.objects.order_by('product_category_name')
    
    # Đọc danh sách Product_brand
    list_brand = Product_brand.objects.order_by('product_brand_name')
    
    # Product detail
    product = Product.objects.get(pk=pk)
    print(product)
    
    return render(request, 'sale_agreement/product_detail.html', {
        'list_category' : list_category,
        'list_brand' : list_brand,
        'product': product,
        
    })
    
    
    
def customer_channel_filter(request, pk):
        # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    # Đọc danh sách Type
    list_type = Customer_type.objects.order_by('customer_type_abbrev')
    # Đọc danh sách Sale area
    list_sale_area = Sale_area.objects.order_by('sale_area_code')
    # Đọc danh sách Province
    list_province = Province.objects.order_by('province_code')
    
    # Đọc danh sách sản phẩm theo Channel
    if pk == 0:
        customers = Customer.objects.order_by('-created_at')
    else:
        customers = Customer.objects.filter(channel=pk).order_by('-created_at')

    # Create customer
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer_channel_filter/0/')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(customers, 15)
    customer_pager = paginator.page(page)
  
    return render(request, 'sale_agreement/customer.html', {
        'form' : form,
        'list_channel' : list_channel,
        'customers': customer_pager,
        'list_type' : list_type,
        'list_sale_area' : list_sale_area,
        'list_province' : list_province
        
        
    }) 

def customer_type_filter(request, pk):
        # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    # Đọc danh sách Type
    list_type = Customer_type.objects.order_by('customer_type_abbrev')
    # Đọc danh sách Sale area
    list_sale_area = Sale_area.objects.order_by('sale_area_code')
    # Đọc danh sách Province
    list_province = Province.objects.order_by('province_code')
    
    # Đọc danh sách sản phẩm theo Type
    if pk == 0:
        customers = Customer.objects.order_by('-created_at')
    else:
        customers = Customer.objects.filter(customer_type=pk).order_by('-created_at')

    # Create customer
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer_type_filter/0/')
    
    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(customers, 15)
    customer_pager = paginator.page(page)
  
    return render(request, 'sale_agreement/customer.html', {
        'form' : form,
        'list_channel' : list_channel,
        'customers': customer_pager,
        'list_type' : list_type,
        'list_sale_area' : list_sale_area,
        'list_province' : list_province
    })
    
def customer_salearea_filter(request, pk):
        # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    # Đọc danh sách Type
    list_type = Customer_type.objects.order_by('customer_type_abbrev')
    # Đọc danh sách Sale area
    list_sale_area = Sale_area.objects.order_by('sale_area_code')
    # Đọc danh sách Province
    list_province = Province.objects.order_by('province_code')
    
    # Đọc danh sách sản phẩm theo Sale Area
    if pk == 0:
        customers = Customer.objects.order_by('-created_at')
    else:
        customers = Customer.objects.filter(sale_area=pk).order_by('-created_at')

    # Create customer
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer_salearea_filter/0/')

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(customers, 15)
    customer_pager = paginator.page(page)
  
    return render(request, 'sale_agreement/customer.html', {
        'form' : form,
        'list_channel' : list_channel,
        'customers': customer_pager,
        'list_type' : list_type,
        'list_sale_area' : list_sale_area,
        'list_province' : list_province
    })
    
def customer_province_filter(request, pk):
        # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    # Đọc danh sách Type
    list_type = Customer_type.objects.order_by('customer_type_abbrev')
    # Đọc danh sách Sale area
    list_sale_area = Sale_area.objects.order_by('sale_area_code')
    # Đọc danh sách Province
    list_province = Province.objects.order_by('province_code')
    
    # Đọc danh sách sản phẩm theo Province
    if pk == 0:
        customers = Customer.objects.order_by('-created_at')
    else:
        customers = Customer.objects.filter(province=pk).order_by('-created_at')

    # Creat Customer
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer_province_filter/0/')
    
    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(customers, 15)
    customer_pager = paginator.page(page)
  
    return render(request, 'sale_agreement/customer.html', {
        'form' : form,
        'list_channel' : list_channel,
        'customers': customer_pager,
        'list_type' : list_type,
        'list_sale_area' : list_sale_area,
        'list_province' : list_province
    })
    
def search_customer(request):
        # Kiểm tra session xem khách hàng đã đăng nhập chưa?
    if 's_user' not in request.session:
        return redirect('sale_agreement:signin')
    
    # Đọc danh sách Channel
    list_channel = Channel.objects.order_by('channel_name')
    # Đọc danh sách Type
    list_type = Customer_type.objects.order_by('customer_type_abbrev')
    # Đọc danh sách Sale area
    list_sale_area = Sale_area.objects.order_by('sale_area_code')
    # Đọc danh sách Province
    list_province = Province.objects.order_by('province_code')
    
    # Tìm kiếm
    customers = []
    keyword = ''
    result_search = ''
    if request.GET.get('customer_name'):
        keyword = request.GET.get('customer_name').upper()
        customers = Customer.objects.filter(customer_name__contains=keyword).order_by('-created_at')
        print(customers)
        
        # Phân trang
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 15)
        customers_pager = paginator.page(page)

    return render(request, 'sale_agreement/customer.html', {
        'list_channel' : list_channel,
        'list_type' : list_type,
        'list_sale_area' : list_sale_area,
        'list_province' : list_province,
        'customers': customers_pager,
        'category_name': result_search,
        'product_name': keyword,
    })
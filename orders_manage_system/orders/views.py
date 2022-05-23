from django.shortcuts import render, redirect, reverse
from . models import ExcelData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.db.models import Q


ACTIVE_INFO = {
    'BillNO': 0,
    '4Digit': 0,
    'HSCode': 0,
    'ForeignCounty': "",
    'Invoice_No': "",
    'keyword': "",
}


# show home page
def index(request):
    # get all info
    data_list = ExcelData.objects.all().values()
    # =========== filter ===========
    if ACTIVE_INFO['BillNO'] != 0:
        data_list = data_list.filter(billno__exact=ACTIVE_INFO['BillNO'])
    if ACTIVE_INFO['4Digit'] != 0:
        data_list = data_list.filter(number_4digit__exact=ACTIVE_INFO['4Digit'])
    if ACTIVE_INFO['HSCode'] != 0:
        data_list = data_list.filter(hscode__exact=ACTIVE_INFO['HSCode'])
    if ACTIVE_INFO['ForeignCounty'] != "":
        data_list = data_list.filter(foreigncountry__icontains=ACTIVE_INFO['ForeignCounty'])
    if ACTIVE_INFO['Invoice_No'] != "":
        data_list = data_list.filter(invoice_no__icontains=ACTIVE_INFO['Invoice_No'])
    if ACTIVE_INFO['keyword'] != "":
        data_list = data_list.filter(Q(product__icontains=ACTIVE_INFO['keyword']) |
                                     Q(indiancompany__icontains=ACTIVE_INFO['keyword']) |
                                     Q(foreigncompany__icontains=ACTIVE_INFO['keyword']))
    # =========== pagination ===========

    paginator = Paginator(data_list, settings.PRE_PAGE_NUMBER)
    # get current page
    number = request.GET.get('page')
    # get current data
    try:
        current_page_orders = paginator.page(number)
    except PageNotAnInteger:
        current_page_orders = paginator.page(1)
    except EmptyPage:
        current_page_orders = paginator.page(paginator.num_pages)

    return render(request, 'index.html', context={'data': current_page_orders})


# show detail page
def show_detail(request):
    index = request.GET.get('index')
    data = ExcelData.objects.filter(index__exact=index).values()
    return render(request, 'detail.html', context={'data': data})


# update keyword
def get_keyword(request):
    # get keyword
    word = request.GET.get('keyword')
    # update
    ACTIVE_INFO['keyword'] = word
    # redirect
    return redirect(reverse('home'))


def search(request):
    billno = request.GET.get("billno")
    # print(billno)
    if billno != "null":
        ACTIVE_INFO['BillNO'] = int(billno)
    digit = request.GET.get("digit")
    print(digit)
    if digit != "null":
        ACTIVE_INFO['4Digit'] = int(digit)
    hscode = request.GET.get("hscode")

    if hscode != "null":
        ACTIVE_INFO['HSCode'] = int(hscode)
    foreigncountry = request.GET.get("foreigncountry")
    if foreigncountry != "null":
        ACTIVE_INFO['ForeignCounty'] = foreigncountry
    invoice_no = request.GET.get("invoice_no")
    if invoice_no != "null":
        ACTIVE_INFO['Invoice_No'] = invoice_no

    return redirect(reverse('home'))


def get_all(request):
    # reset
    ACTIVE_INFO['BillNO'] = 0
    ACTIVE_INFO['4Digit'] = 0
    ACTIVE_INFO['HSCode'] = 0
    ACTIVE_INFO['ForeignCounty'] = ""
    ACTIVE_INFO['Invoice_No'] = ""
    ACTIVE_INFO['keyword'] = ""

    return redirect(reverse('home'))


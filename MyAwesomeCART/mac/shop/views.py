
from django.shortcuts import render
from.models import Product
from math import ceil
from .models import Rating
from .forms import ReviewForm
from django.contrib.messages import constants as messages
from django.shortcuts import redirect
from .models import Orders , Contact



import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse

# Create your views here.
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')
def about(request):
    return render(request, 'shop/about.html')



def tracker(request):
    return HttpResponse("We are at about.")

def search(request):
    return HttpResponse("We are at about.")

def productView(request, myid):
    # fetch product using id
    product = Product.objects.filter(id=myid )
    return render(request, "shop/prodView.html", {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

def submit_review(request, product_id):
    url = request.META.get('Http_REFERER')
    if request.method == 'POST':
        try:
             reviews = Rating.objects.get(id=request.id , product__id=product_id)
             form = ReviewForm(request.POST, instance=reviews)
             form.save()
             messages.success(request, 'Thank you ypur review has been updated')
             return redirect(url)
        except Rating.DoesNotExist:
          form = ReviewForm(request.POST)
          if form.is_valid():
                data = Rating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you ypur review has been submitted')
                return redirect(url)







def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')
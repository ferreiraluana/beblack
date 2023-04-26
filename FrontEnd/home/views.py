from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import CartProduct
from django.shortcuts import redirect
import requests
import pandas as pd

# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def APIrequest(request):
    response = ''
    try:
        json = requests.get('http://127.0.0.1:5000/products')
        response = "API Connection Success! / Database Updated!"
    except:
        response = "Failed to Connect to API"
    
    if(response == "API Connection Success! / Database Updated!"):
        products = pd.read_json(json.text)
        row_iter = products.iterrows()
        objs = [
            Product(
                name = row['name'],
                vendor  = row['vendor'],
                price  = row['price'],
                imageUrl = row['imageUrl']
            )
            for index, row in row_iter
        ]

        Product.objects.bulk_create(objs)

    return render(request, 'api.html', {'response': response})

def index(request):
    data = {}

    data['products'] = Product.objects.all()

    return render(request, 'index.html', data)

def search(request):
    query = request.GET.get('query')
    products = {}
    if query:
        products = Product.objects.filter(name__icontains=query)

    return render(request, 'search.html', {'products': products, 'query': query})

def cart(request):
    buyThis = request.GET.get('buyThis')
    delete = request.GET.get('delete')
    deleteAll = request.GET.get('deleteAll')
    if(buyThis):
        productToBuy = Product.objects.filter(id = buyThis).first()
        productToBuy.name
        newProduct = CartProduct(name=productToBuy.name, vendor=productToBuy.vendor, price=productToBuy.price, imageUrl=productToBuy.imageUrl, customer=request.user)
        newProduct.save()
        return redirect('/cart')
    if delete:
        productToDelete = CartProduct.objects.filter(name = delete).filter(customer=request.user).first()
        productToDelete.delete()
        return redirect('/cart')
    if deleteAll:
        productsToDelete = CartProduct.objects.filter(customer=request.user)
        productsToDelete.delete()
        return redirect('/cart')
    
    products = CartProduct.objects.filter(customer=request.user)
    sum = 0
    for product in products:
        sum += product.price

    return render(request, 'cart.html', {'products': products, 'total': sum})
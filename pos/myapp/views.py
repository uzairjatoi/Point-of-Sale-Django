from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import*
from django.forms import modelform_factory
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'invalid credentials')
            return redirect ('login')
        else:
            login(request, user)
            return redirect ('home')
        
    return render(request, 'login.html') 
def logout_page(request):
    logout(request)
    return redirect ('login')   
    


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username,)
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('register')
        

        user.set_password(password)
        user.save()
        messages.info(request, 'Account Created successfully')
        return redirect ('home')
    return render(request, 'register.html')


@login_required(login_url="login")
def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store.html', {'stores': stores})



@login_required(login_url="login")
def create_store(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        store = Store.objects.create(name=name, location=location)
        return redirect('store_list')
    return render(request, 'create_store.html')



@login_required(login_url="login")
def update_store(request):
    stores = Store.objects.all()
    if request.method == 'POST':
        store_id = request.POST.get('store_id')
        store = get_object_or_404(Store, id=store_id)
        store.name = request.POST['name']
        store.location = request.POST['location']
        store.save()
        return redirect('store_list')
    return render(request, 'update_store.html', {'stores': stores,})


@login_required(login_url="login")
def delete_store(request):
    stores = Store.objects.all()
    if request.method == 'POST':
        store_id = request.POST.get('store_id')
        store = get_object_or_404(Store, id=store_id) 
        store.delete()
        return redirect('store_list')
    return render(request, 'delete_store.html', {'stores': stores})



@login_required(login_url="login")
def inventory_list(request):
    inventory = Inventory.objects.all()
    return render (request, 'inventory_list.html', {'inventory': inventory})



@login_required(login_url="login")
def create_inventory(request):
    
    if request.method == 'POST':
        store_name = request.POST.get('store')
        product_name = request.POST.get('product')
        quantity = request.POST.get('quantity')
        store = get_object_or_404(Store, name=store_name)
        product, created = Product.objects.get_or_create(name=product_name)
        inventory = Inventory.objects.create(store=store, product=product, quantity=quantity)
        return redirect('inventory_list')
    stores = Store.objects.all()
    products = Product.objects.all()
    return render(request, 'create_inventory.html', {'stores' : stores, 'products' : products})


@login_required(login_url="login")
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale_list.html', {'sales' : sales})



@login_required(login_url="login")
def create_sale(request):
    SaleForm = modelform_factory(Sale, exclude=('date',))
    stores = Store.objects.all()
    customers = Customer.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.price = sale.product.price
            sale.date = timezone.now().date()
            sale.save()
            inventory = get_object_or_404(Inventory, store=sale.store, product=sale.product)
            inventory.quantity -= sale.quantity
            inventory.save()
            return redirect('salelist')
    else:
        form = SaleForm()
    return render(request, 'create_sale.html', {'form': form, 'stores': stores, 'customers': customers, 'products': products})




@login_required(login_url="login")
def create_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        customer = Customer.objects.create(name=name, phone=phone, email=email)
        return redirect('customerdetail')
    return render(request, 'createcustomer.html')



@login_required(login_url="login")
def customerdetail(request):
    customers = Customer.objects.all()
    return render(request, 'customerdetail.html', {'customers': customers})



@login_required(login_url="login")
def update_customer(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        customer = get_object_or_404(Customer, id=customer_id)
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.save()
        return redirect('customerdetail')
    return render(request, 'updatecustomer.html', {'customers': customers})



@login_required(login_url="login")
def delete_customer(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()
        return redirect('customerdetail')
    return render(request, 'deletecustomer.html', {'customers': customers})



@login_required(login_url="login")
def createproduct(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        brand = request.POST.get('brand')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        image = request.POST.get('image')
        price = request.POST.get('price')
        cost = request.POST.get('cost')
        supplier_name = request.POST.get('supplier_name')
        supplier = get_object_or_404(Supplier, name = supplier_name)
        product = Product.objects.create(name = name, description = description, brand = brand, category = category, supplier = supplier, sub_category = subcategory, image = image, price = price, cost = cost)
        return redirect('productdetail')
    return render(request, 'product.html', {'suppliers' : suppliers})


@login_required(login_url="login")
def productdetail(request):
    products = Product.objects.all()
    return render(request, 'productdetail.html', {'products': products})


@login_required(login_url="login")
def update_product(request):
    
    suppliers = Supplier.objects.all()
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.brand = request.POST.get('brand')
        product.category = request.POST.get('category')
        product.sub_category = request.POST.get('sub_category')
        product.image = request.FILES.get('image', product.image)
        product.price = request.POST.get('price')
        product.cost = request.POST.get('cost')
        supplier_name = request.POST.get('supplier_name')
        supplier = get_object_or_404(Supplier, name=supplier_name)
        product.supplier = supplier
        product.save()
        return redirect('productdetail')

    return render(request, 'update_product.html', {'products': products, 'suppliers': suppliers})


@login_required(login_url="login")
def delete_product(request):

    products = Product.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('productdetail')
    
    return render(request, 'deleteproduct.html', {'products': products})
    


@login_required(login_url="login")
def payment_options(request):
    payment_options = PaymentOption.objects.all()
    if request.method == 'POST':
        selected_option = request.POST.get('payment_option')
        payment = PaymentOption.objects.create(name = selected_option)
        return redirect('createsale')
    return render(request, 'payment_options.html', {'payment_options': payment_options})


@login_required(login_url="login")
def createsupplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        supplier = Supplier.objects.create(name=name, email=email, phone=phone)
        return redirect('main')
    return render(request, 'createsupplier.html')


@login_required(login_url="login")
def supplierdetail(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplierdetail.html', {'suppliers': suppliers})


@login_required(login_url="login")
def main (request):
    return render(request, 'main.html')












        







       







"""
URL configuration for pos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', login_page, name='login'),
    path('logout', logout_page, name='logout'),
    path('register/', register_user, name='register'),
    path('main', main, name='home'),
    path('createsupplier/', createsupplier, name='createsupplier'),
    path('supplierdetail/', supplierdetail, name='supplierdetail'),
    path('storelist/', store_list, name='store_list'),
    path('createstore/', create_store, name = 'createstore' ),
    path('updatestore/',update_store, name='update_store'),
    path('deletestore/',delete_store, name='delete_store'),
    path('inventorylist/', inventory_list, name='inventory_list'),
    path('createinventory/', create_inventory, name='create_inventory'),
    path('createsale/', create_sale, name='createsale'),
    path('salelist/', sale_list, name='salelist'),
    path('createcustomer/', create_customer, name='createcustomer'),
    path('updatecustomer/', update_customer, name='updatecustomer'),
    path('deletecustomer/', delete_customer, name='deletecustomer'),
    path('customerdetail/', customerdetail, name='customerdetail'),
    path('createproduct/', createproduct, name='createproduct'),
    path('productdetail/', productdetail, name='productdetail'),
    path('update_product/',update_product, name='update_product'),
    path('deleteproduct/', delete_product, name='deleteproduct'),
    path('paymentoption/', payment_options, name='paymentoption'),
    path('admin/', admin.site.urls),
    
]

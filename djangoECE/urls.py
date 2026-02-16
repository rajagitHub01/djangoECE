"""ECE_Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from djangoECE_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about', views.aboutuspage),
    path('login', views.loginform),
    path('home', views.home2),  
    path('addproduct_page', views.addproduct_page, name = "addproduct_page"),
    path('modify_page', views.modify_page),
    path('search_page/', views.search_page, name='search_page'),


    # Logical FUnctions #
    path('register', views.user_register),
    path('userlogin', views.user_login),
    path('logout', views.logout),
    path('afterlogin', views.after_login_homepage, name = "afterlogin"),
    path('addproduct', views.add_product),
    path('search_product/', views.search_product, name='search_product'),
    path('update/<int:id>/', views.product_details_update, name="update"),
    path('delete/<int:id>/', views.product_details_delete, name="delete"),

    # for API 
    path('api/products', views.addProduct_API),
    path('api/products/<int:id>/', views.all_product_details),

]

"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from pages.views import home_view, about_view, contact_view
from products.views import product_detail_view,product_create_view,raw_product_create_view
#from users.views import register, profile
from customer.views import register, profile
from django.contrib.auth import views as auth_views
urlpatterns = [
	#path('pool/', include('pool.urls')),
    path('store/',include('bookstore.urls')),
    #path('customer/book/',book),
    path('customer/register/',register),
    path('customer/profile/',profile),
    path('customer/login/',auth_views.LoginView.as_view(template_name = 'customer/login.html'), name="login"),
    path('customer/logout/',auth_views.LogoutView.as_view(template_name = 'customer/logout.html'), name="logout"),
	path('about/', about_view),
    path('blog/register/',register),
    path('blog/profile/',profile),
    #path('blog/login/',auth_views.LoginView.as_view(template_name = 'form/login.html'), name="login"),
   # path('blog/logout/',auth_views.LogoutView.as_view(template_name = 'form/logout.html'), name="logout"),
    path('blog/',include('blog.urls')),
	path('contact/', contact_view),
	path('', home_view, name='home'),
	path('checkproduct/', product_detail_view),
	path('productform/', raw_product_create_view),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.shortcuts import render
from .models import Product
# Create your views here.
from .forms  import ProductForm, RawProductForm

def raw_product_create_view(request):
	form = RawProductForm(request.POST)
	if form.is_valid():
		print(form.cleaned_data)
		Product.objects.create(**form.cleaned_data)
	cont = {
		"form":form,
	}
	return render(request,"form/product_create.html",cont)
 

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		'form':form,
	}
	return render(request,"form/product_create.html",context)



def product_detail_view(request):
	obj = Product.objects.get(id=1);
	#prod = {
	#	"title":obj.title,
	#	"description":obj.description,
	#	"price":obj.price,
	#	"abc":obj.feedback,
	#}
	prod = {
		"obtt":obj,
	}
	return render(request ,"products/detail.html",prod)
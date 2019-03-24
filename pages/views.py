from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
	print(request.user)
	print(args, kwargs)
	return render(request,"home.html", {})

def about_view(request,*args, **kwargs):
	about = {
		"name": "ashutosh kumar singh",
		"age":20,
		"list":[12,13,14,20],
	}
	return render(request,"about.html", about)

def contact_view(request,*args, **kwargs):
	#print(request.user)
	#print(args, kwargs)
	return render(request,"contact.html", {})
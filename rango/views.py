from django.shortcuts import render
from django.http import HttpResponse

#Chapter 3
#def index(request):
#    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>") 
	
def index(request):
	context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context = context_dict)

#Chapter 3	
#def about(request):
#	return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")

def about(request):
	some_dict = {'somemessage' : "This tutorial has been put together by Koh Pi Shing."}
	return render(request, 'rango/about.html', context = some_dict)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import menu_lang, menu_items
# Create your views here.
def menu(request):
	
	return render(request, 'menu.html', context={
		'menu': menu_items.objects.all(),
		'lang': menu_lang.objects.get()
		})
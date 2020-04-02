from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from login.models import worker
from filmstudio.models import filmstudio_inventory
from repair.models import menu as repair_menu
from foodstore.models import menu as foodstore_menu
from login.views import is_worker
# Create your views here.
def lister(text):
	listing = []
	text = text.replace("\r","")
	for i in text.split("\n"):
		listing.append(i.split("\t"))
	for i in range(len(listing)): # no empty rows
		if listing[i] == [""]:
			listing.remove(listing[i])
	return listing

def loader(request):
	is_worker(request)

	if request.POST:
		items = lister(request.POST["sisu"])
		if request.POST["table"] == "foodstore":
			if request.POST["delete"] == "yes":
				foodstore_menu.objects.filter(lang=items[0][0]).delete()
			for item in items:
				foodstore_menu.objects.create(lang=item[0], item_cat=item[1], item_name=item[2], item_price=item[3])
		if request.POST["table"] == "repair":
			if request.POST["delete"] == "yes":
				repair_menu.objects.filter(lang=items[0][0]).delete()
			for item in items:
				repair_menu.objects.create(lang=item[0], item_cat=item[1], item_name=item[2], item_price=item[3])
		if request.POST["table"] == "filmstudio":
			if request.POST["delete"] == "yes":
				filmstudio_inventory.objects.all().delete()
			for item in items:
				filmstudio_inventory.objects.create(item=item[0], desc=item[1], qty=item[2])


	return render(request, 'loader.html', context={
		
		})
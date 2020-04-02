from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import reklaam_entry
from login.models import worker
from login.views import is_worker
# Create your views here.
def reklaam(request):
	request.session['paper'] = '-'
	is_worker(request)

	items = reklaam_entry.objects.all()
	if bool(request.POST) == True:
		request.session['paper'] = request.POST['submit-btn']
		items = reklaam_entry.objects.filter(nimi=request.POST['submit-btn'])

	return render(request, 'reklaam.html', context={
		'items': items
		})
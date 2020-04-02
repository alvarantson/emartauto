from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import varuosad_entry, google_link
from login.models import worker
from login.views import is_worker
# Create your views here.
def varuosad(request):
	is_worker(request)


#	if bool(request.POST) == True:

#		if 'remove' in request.POST['submit-btn']:
#			varuosad_entry.objects.get(
#				nr=request.POST['submit-btn'].split('-')[1].split('~')[0],
#				aeg=request.POST['submit-btn'].split('-')[1].split('~')[1]
#			).delete()

#		if 'new' in request.POST['submit-btn']:
#			try:
#				nr = str(int(varuosad_entry.objects.last().nr)+1)
#			except:
#				nr = 1
#			varuosad_entry.objects.create(
#				nr = nr,
#				nimi = request.POST['nimi'],
#				kontakt = request.POST['kontakt'],
#				automark = request.POST['automark'],
#				varuosade_kood = request.POST['varuosade_kood'],
#				nimetus = request.POST['nimetus'],
#				hind = request.POST['hind'],
#				kogus = request.POST['kogus'],
#				tellitud_kuup = request.POST['tellitud_kuup'],
#				saabus_kuup = request.POST['saabus_kuup'],
#				valja_kuup = request.POST['valja_kuup'],
#				ettemaks = request.POST['ettemaks'],
#				aeg = request.POST['aeg'],
#				kes_tegi = request.POST['kes_tegi']
#			)

#		if 'edit' in request.POST['submit-btn']:
#			edit = varuosad_entry.objects.get(nr=request.POST['nr'], aeg=request.POST['aeg'])
#			edit.nimi = request.POST['nimi']
#			edit.kontakt = request.POST['kontakt']
#			edit.automark = request.POST['automark']
#			edit.varuosade_kood = request.POST['varuosade_kood']
#			edit.nimetus = request.POST['nimetus']
#			edit.hind = request.POST['hind']
#			edit.kogus = request.POST['kogus']
#			edit.tellitud_kuup = request.POST['tellitud_kuup']
#			edit.saabus_kuup = request.POST['saabus_kuup']
#			edit.valja_kuup = request.POST['valja_kuup']
#			edit.ettemaks = request.POST['ettemaks']
#			edit.kes_tegi = request.POST['kes_tegi']
#			edit.save()

#		return HttpResponseRedirect('/varuosad')

#	if len(varuosad_entry.objects.all()) != 0:
#		new_nr = str(int(varuosad_entry.objects.all()[len(varuosad_entry.objects.all())-1].nr)+1)
#	else:
#		new_nr = 1
#	return render(request, 'varuosad.html', context={
#		'items':varuosad_entry.objects.all().reverse(),
#		'new_nr': new_nr
#		})


	return render(request, 'kalender.html', context={
		'link':google_link.objects.first()
		})
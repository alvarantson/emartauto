from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs, ad, social_media
from .models import foodstore_lang, menu
# Create your views here.
def foodstore(request):
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/foodstore') #INDEX\i puhul '/'
	ad2 = []
	for nr in range(len(ad.objects.all())):
		ad2.append(nr)
	return render(request, 'foodstore.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'lang': foodstore_lang.objects.get(lang=request.session['lang']),
		'menu': menu.objects.filter(lang=request.session['lang']),
		'ads':ad.objects.all(),
		'ads2':ad2,
		'social_media':social_media.objects.all()
		})
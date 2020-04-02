from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs, ad, social_media
from .models import filmstudio_lang, filmstudio_img, filmstudio_inventory, filmstudio_vid
from statistika.views import collect_statistics
# Create your views here.
def filmstudio(request):
	collect_statistics(request, "filmstudio")
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/filmstudio') #INDEX\i puhul '/'
	ad2 = []
	for nr in range(len(ad.objects.all())):
		ad2.append(nr)
	return render(request, 'filmstudio.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'lang': filmstudio_lang.objects.get(lang=request.session['lang']),
		'img': filmstudio_img.objects.all(),
		'inventory': filmstudio_inventory.objects.all(),
		'ads':ad.objects.all(),
		'ads2':ad2,
		'social_media':social_media.objects.all(),
		'videos': filmstudio_vid.objects.all()
		})
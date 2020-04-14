from django.shortcuts import render
from foodstore.models import menu as menuu
# Create your views here.
def menu(request):
	return render(request, 'menu.html', context={
		"menu":menuu.objects.filter(lang="est")
		})
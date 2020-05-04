from django.shortcuts import render
from login.views import is_worker
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def rmp(request):
	auth = "n"
	try:
		if request.session["rmp_priority"]:
			auth = "y"
	except:
		pass
	asd = [
		{"name": "VALKLA 2020", "link": "1PvsknmxFNYztPiGI0Ckai9mORNLnfCSDisptKPm-t2M"},
		{"name": "KUUSALU 2020", "link": "1Sk3HGPfs786UnDftRo5Aby1izg9POvLQ6qe6ZwIMGrE"},
		{"name": "HAMBURGER 2020", "link": "1WwRI6B5yYPAMrtMyDc70ihF3RLi2rTknjXC8WqeB6vs"},
		{"name": "EMART AUTO 2020", "link": "13-p3KhBsqOGTPWCdij18R8x-aBJiezDweVXT_kEFElM"},
		{"name": "AUTOPOOD 2020", "link": "1rFAjFjZLvfO2LEIiVNMfD2bKQ8bpgSwsGg4UC8OJbMI"}
		]

	return render(request, "rmp.html", {
		"links": asd,
		"auth": auth
		})


def view(request, asd):
	try:
		if not request.session["rmp_priority"]:
			return HttpResponseRedirect("/rmp")
	except:
		pass

	asd = "https://docs.google.com/spreadsheets/d/"+asd+"/edit?usp=sharing"
	return render(request, "kalender.html", {
		"link":{"link":asd},
		"rmp":"y"
		})
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
		{"name": "VALKLA 2022", "link": "1qM6tm3KFDYM3C5DRSFNhRJ97VvOOD1QG8MoBL1dJrH4"},
		{"name": "KUUSALU 2022", "link": "1_6OO8c3YyKLXuVsiK1Q0rpaRNaiHbQV1-cfEDbACA_o"},
		{"name": "HAMBURGER 2022", "link": "1ZsyarHw4QzB_fFgOUyM7UNgRVrX63afNBsa8ypkmJao"},
		{"name": "EMART AUTO 2022", "link": "1iC_vF_pOabZr13zinjk1BI_5iJ9dDvSm2p5NxPmgnAc"},
		{"name": "AUTOPOOD 2022", "link": "1BnOC8j6zbmVxjOQh2jBAOHZ62MU_M67wSfCCrcE2toc"},
		{"name": " "},
		{"name": "VALKLA 2021", "link": "1vvZFqZQ9MuaXIAn1dqd-OGiQePG_I_gqGVrmEZtrF_g"},
		{"name": "KUUSALU 2021", "link": "1QtUaDGjPSkXF_Y-AN7RezJaBIXTYozjVCzDU3sAJntU"},
		{"name": "HAMBURGER 2021", "link": "1eupNMt8Qxh0CKuR7PdHYt8YFpPrw9v-3wGK1yMY7_xo"},
		{"name": "EMART AUTO 2021", "link": "1-EseiSl1ZRUSGTYQwKRWUtzAxJ3863rjI1EM06avyEI"},
		{"name": "AUTOPOOD 2021", "link": "1iCFsU3ferOu-zlhU7opd5d53DOzMzPh-TlWq4WEuVmU"},
		{"name": "uus", "link": "1oVqKu1NyGbplMXAnMkkWU0oRW2OysVYMQ7K922i7NKA"},
		{"name": "VALKLA 2020", "link": "1PvsknmxFNYztPiGI0Ckai9mORNLnfCSDisptKPm-t2M"},
		{"name": "KUUSALU 2020", "link": "1Sk3HGPfs786UnDftRo5Aby1izg9POvLQ6qe6ZwIMGrE"},
		{"name": "HAMBURGER 2020", "link": "1WwRI6B5yYPAMrtMyDc70ihF3RLi2rTknjXC8WqeB6vs"},
		{"name": "EMART AUTO 2020", "link": "13-p3KhBsqOGTPWCdij18R8x-aBJiezDweVXT_kEFElM"},
		{"name": "AUTOPOOD 2020", "link": "1rFAjFjZLvfO2LEIiVNMfD2bKQ8bpgSwsGg4UC8OJbMI"},
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
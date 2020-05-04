from django.conf.urls import url, re_path
from . import views

urlpatterns = [
	re_path(r'^view/(?P<asd>.*)$', views.view),
    url(r"^$", views.rmp)
]
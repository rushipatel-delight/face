from django.conf.urls import url
from book import views

urlpatterns = [
	url(r'^login$/',views.login_page,name = 'login_page'),
	url(r'^check$/',views.log_check)
]
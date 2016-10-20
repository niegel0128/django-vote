from django.conf.urls import url
from . import views

app_name = 'elections' #layout.html 의 네이베이션바에서 elections : home 을 사용하기위해 추가
urlpatterns = [
	url(r'^$', views.index, name = 'home'), #layout.html 의 네이베이션바에서 elections : home 을 사용하기위해 추가
	url(r'^areas/(?P<area>[가-힣]+)/$', views.areas), #.+는 모든 url을 허용하겠다는뜻
	url(r'^areas/(?P<area>[가-힣]+)/results$', views.results), #[가-힣]모든 한글만 허용하겠다는뜼
	url(r'^polls/(?P<poll_id>\d+)/$', views.polls), #이 url에 대한 요청을 views.polls가 처리하게 만듭니다.
]

from django.conf.urls import url

from messages import views

urlpatterns = [
    url(r'^message/$', views.MessagesCreate.as_view()),
    url(r'^report/(?P<chat_id>[0-9]+)/$', views.ReportList.as_view())
]

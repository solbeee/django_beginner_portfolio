from django.conf.urls import url
from helloworld import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^about/contact/$', views.ContactPageView.as_view()),
    url(r'^about/contact/projects/$', views.ProjectsPageView.as_view()),
]

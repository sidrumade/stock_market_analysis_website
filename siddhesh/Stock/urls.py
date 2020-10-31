from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index,name='index') ,
    path('index.html', views.index,name='index') ,
    path('home.html', views.home,name='home') ,
    path('singlegraph.html',views.singlegraph,name='singlegraph') ,
    path('shownifty50.html', views.shownifty50,name='shownifty50') ,
    



]

urlpatterns += staticfiles_urlpatterns()
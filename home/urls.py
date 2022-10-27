from django.urls import path
from home import views


urlpatterns = [
    path('a',views.about,name="about"),
    path('',views.home,name="home"),
    

]

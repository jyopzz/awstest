from . import views
from django.urls import path,include
from .views import loginn
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [
    #path('', loginn),
    path ('accounts/',include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    #path('main/',TemplateView.as_view(template_name='main.html'),name='main'),
     path('main/',views.main,name='main'),
     #path('main/getname',views.getname,name="getname"),
    path('main/insert/',views.insertdata,name="insertdata"),
    path('edit/<id>/',views.edit,name="edit"),
    
    path('delete/<id>/',views.delete,name="delete"),
]
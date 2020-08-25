
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name='welcome'),
    path('load_form',views.load_form,name='load_form'),
    path('add',views.add,name='add'),
    path('show',views.show,name='show'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('search',views.search),
    path('register',views.register),
    path('addd',views.addd),
    path('watch',views.watch),
    path('editt/<int:id>',views.editt),
    path('Gro',views.Gro),
    path('details',views.details),
    path('Adddd',views.Adddd),
    path('regi', views.regi),
    path('Dele/<int:id>',views.Dele),
    path('sea',views.sea),
   
]

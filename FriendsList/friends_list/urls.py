from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('additional', views.add_to_list, name='additional'),
    path('show', views.show_all_list, name='show'),
    path('contact', views.contact, name='contact'),
    ]

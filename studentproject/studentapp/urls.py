from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    # path('add/', views.addition, name='addition'),
    # path('name', views.name, name='name'),
    # path('vijin', views.vijin, name='vijin'),
    # path('final', views.final, name='final')

]

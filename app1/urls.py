from django.urls import path
from . import views

urlpatterns = [
    path('rana',views.rana,name = 'rana'),
    path('addition',views.add,name ='add'),

]
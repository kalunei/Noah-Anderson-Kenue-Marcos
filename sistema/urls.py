# arquivo urls.py dentro do app sistema
from django.urls import path
from sistema import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name='index'),
]
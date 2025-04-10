# arquivo urls.py dentro do app sistema
from django.urls import path
from sistema import views

app_name = 'sistema'

urlpatterns = [
    # path('', views.index, name='index'),
    path('funcionarios/', views.listarFuncionario, name='funcionario'),
    path('fornecedores/', views.listarFornecedores, name='fornecedor'),
    path('clientes/', views.listarClientes, name='cliente'),
    path('produtos/', views.listarProdutos, name='produto'),
    
]
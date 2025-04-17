# arquivo urls.py dentro do app sistema
from django.urls import path
from sistema import views

app_name = 'sistema'

urlpatterns = [
    # path('', views.index, name='index'),
    path('funcionarios/', views.listarFuncionario, name='funcionario'),
    path('funcionarios/cadastro/', views.cadastroFuncionario, name='funcionario_cadastro'),
    path('fornecedores/', views.listarFornecedores, name='fornecedor'),
    path('fornecedores/cadastro/', views.cadastroFornecedores, name='fornecedores_cadastro'),
    path('clientes/', views.listarClientes, name='cliente'),
    path('clientes/cadastro/', views.cadastroClientes, name='clientes_cadastro'),
    path('produtos/', views.listarProdutos, name='produto'),
    path('produtos/cadastro/', views.cadastroProdutos, name='produtos_cadastro'),
    
]
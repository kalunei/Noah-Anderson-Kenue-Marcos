from django import forms
from .models import Funcionario
from .models import Fornecedor
from .models import Produto
from .models import Cadastro_cliente


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'cpf', 'salario', 'turno', 'cargo',]

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_comercial', 'cnpj', 'tipo',]

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'validade', 'quantidade_estoque',]

class Cadastro_clienteForm(forms.ModelForm):
    class Meta:
        model =  Cadastro_cliente
        fields = ['nome', 'sobrenome', 'cpf', 'email', 'ativo',]

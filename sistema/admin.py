from django.contrib import admin

from sistema import models 

# Register your models here.

@admin.register(models.Funcionario)
class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'cpf', 'email', 'cargo',)
    search_fields = ('id','nome', 'sobrenome', 'cpf',)


@admin.register(models.Produto)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'preco', 'quantidade_estoque', 'validade', 'codigo',)


@admin.register(models.Cadastro_cliente)
class Cadastro_clienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'cpf', 'ativo',)
    list_editable = ('ativo',)
    list_filter = ('id','nome','cpf',)


@admin.register(models.Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id','nome_comercial','cnpj','tipo',)
    list_filter = ('id','nome_comercial','cnpj',)
    
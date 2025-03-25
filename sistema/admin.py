from django.contrib import admin

from sistema import models 

# Register your models here.

@admin.register(models.Funcionario)
class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email', 'cargo',)
    search_fields = ('nome', 'sobrenome', 'cpf',)


@admin.register(models.Produto)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque', 'validade', 'codigo',)
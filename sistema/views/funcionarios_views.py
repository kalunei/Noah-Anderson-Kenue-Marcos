from django.shortcuts import render, redirect
from sistema.models import Funcionario
from sistema.forms import FuncionarioForm

def listarFuncionario(request):
    funcionarios = Funcionario.objects.all()


    context = {
        'funcionarios': funcionarios,
    }

    return render(
        request,
        'funcionarios/listar.html',
        context,
    )


def cadastroFuncionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES )#request.FILES , só se tiver (imagens etc), request.POST pega tudo do resto(nome,email,cfp....)
        if form.is_valid():
            # se os dados forem válidos é salvo um novo Funcionario no Banco de Dados.
            form.save()
            return redirect('/funcionarios')
        else:
            print("error no Funcionario_views.py - cadastroFuncionarios") 
    elif request.method == 'GET':
        form = FuncionarioForm()
    else: print("error no Funcionario_views.py - cadastroFuncionarios") 
    
    return render(
        request,
        'funcionarios/cadastro.html',
        {'form': form},
    )
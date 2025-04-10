from django.shortcuts import render
from sistema.models import Funcionario


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

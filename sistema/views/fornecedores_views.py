from django.shortcuts import render
from sistema.models import Fornecedor


def listarFornecedores(request):
    fornecedores = Fornecedor.objects.all()


    context = {
        'fornecedores': fornecedores,
    }

    return render(
        request,
        'fornecedores/listar.html',
        context,
    )

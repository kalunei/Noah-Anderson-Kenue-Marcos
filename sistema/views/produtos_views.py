from django.shortcuts import render
from sistema.models import Produto


def listarProdutos(request):
    produtos = Produto.objects.all()


    context = {
        'produtos': produtos,
    }

    return render(
        request,
        'produtos/listar.html',
        context,
    )

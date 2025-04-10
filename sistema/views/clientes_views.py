from django.shortcuts import render
from sistema.models import Cadastro_cliente


def listarClientes(request):
    clientes = Cadastro_cliente.objects.all()


    context = {
        'clientes': clientes,
    }

    return render(
        request,
        'clientes/listar.html',
        context,
    )

from telas import *
from persistencia import *
from Produto import *

def menu():
    limparTela()
    print("-------- Revenda ES --------")
    print("1 - Cadastrar Veículo")
    print("2 - Editar Inventário")
    print("3 - Excluir Veículo")
    print("4 - Selecionar Veículos")
    print("5 - Listar Veículos")
    print("6 - Sair")
    print("-------------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


persistencia = Persistencia()

while True:
    opcao = menu()

    if opcao == 1:
        vei = cadastrarVeículo()
        persistencia.criar(vei)
        exibirMsg("Veículo cadastrado com Sucesso!")
    elif opcao == 2:
        vei = editarVeículo()
        persistencia.editar(vei)
        exibirMsg("Veículo editado com Sucesso!")
    elif opcao == 3:
        limparTela()
        Id = excluirVeículo()
        persistencia.excluir(Id)
        exibirMsg("Veículo excluído com Sucesso!")
    elif opcao == 4:
        Id = selecionarVeículo()
        vei = persistencia.selecionar(Id)
        if vei == None:
            exibirMsg("Veículo não Encontrado!")
        else:
            exibirVeículo(vei)
            travarTela()
    elif opcao == 5:
        vei = persistencia.selecionar_todos()
        exibirVeículos(vei)
    elif opcao == 6:
        break

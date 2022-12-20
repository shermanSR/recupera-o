import os
from Produto import *


def cadastrarVeículo() -> Veículos:
    limparTela()
    print("-------- Cadastro de Veículo --------")
    veiculo = Veículos()
    veiculo.setMarca(input('Marca: '))
    veiculo.setModelo(input('Modelo: '))
    veiculo.setAno(int(input('Ano: ')))
    veiculo.setCor(input('Cor: '))
    veiculo.setCambio(input('Câmbio: '))

    return veiculo


def editarVeículo() -> Veículos:
    limparTela()
    print("-------- Edição de Veículo --------")
    veiculo = Veículos()
    veiculo.setId(int(input('Placa: ')))
    veiculo.setMarca(input('Marca: '))
    veiculo.setModelo(input('Modelo: '))
    veiculo.setAno(int(input('Ano: ')))
    veiculo.setCor(input('Cor: '))
    veiculo.setCambio(input('Câmbio: '))
    return veiculo


def excluirVeículo():
    print("-------- Exclusão de Veículo --------")
    limparTela()
    Placa = int(input('Placa: '))
    return Placa


def selecionarVeículo():
    limparTela()
    print("-------- Seleção de Veículo --------")
    Placa = int(input('Placa: '))
    return Placa


def exibirVeículo(Veículo: Veículos):
    print("-------- Veículo --------")
    print(f"Placa: {Veículo.getId()}")
    print(f"Marca: {Veículo.getMarca()}")
    print(f"Modelo: {Veículo.getModelo()}")
    print(f"Ano: {Veículo.getAno()}")
    print(f"Cor: {Veículo.getCor()}")
    print(f"Câmbio: {Veículo.getCambio()}")


def exibirVeículos(Veículos):
    limparTela()
    print("----------- Veículos -----------")
    for Veículo in Veículos:
        exibirVeículo(Veículo)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para retornar ao Menu.')


def exibirMsg(msg):
    print(msg)
    travarTela()

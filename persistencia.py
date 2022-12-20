from json_storage import *
from Produto import *



class Persistencia():
    __storage = JsonStorage()

    def criar(self, dado: Veículos) -> Veículos:
        dados = self.selecionar_todos()
        dado.setId(self.__gerarId())
        dados.append(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def editar(self, dado: Veículos) -> None:
        dados = self.selecionar_todos()
        for i, data in enumerate(dados):
            if data.getId() == dado.getId():
                dados[i] = dado.toDict()
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def excluir(self, id: int) -> None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                dados.remove(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def selecionar(self, Id: int):
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == Id:
                return dado
        return None

    def selecionar_todos(self):
        Veiculos = []
        for i in self.__storage.lerJson():
            veiculo = Veículos()
            veiculo.setId(i['Id'])
            veiculo.setMarca(i['Marca'])
            veiculo.setModelo(i['Modelo'])
            veiculo.setAno(i['Ano'])
            veiculo.setCor(i['Cor'])
            veiculo.setCambio(i['Cambio'])
            Veiculos.append(veiculo)
        return Veiculos

    def __gerarId(self) -> int:
        dados = self.selecionar_todos()
        if len(dados) == 0:
            return 1
        return dados[-1].getId() + 1

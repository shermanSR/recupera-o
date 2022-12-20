class Veículos():
    __Id: int
    __Marca: str
    __Modelo: str
    __Ano: int
    __Cor:str
    __Câmbio:str

    def getId(self):
        return self.__Id

    def setId(self, Id):
        self.__Id = Id

    def getMarca(self):
        return self.__Marca

    def setMarca(self, marca):
        self.__Marca = marca

    def getModelo(self):
        return self.__Modelo

    def setModelo(self, modelo):
        self.__Modelo = modelo

    def getAno(self):
        return self.__Ano

    def setAno(self, ano):
        self.__Ano = ano

    def getCor(self):
        return self.__Cor

    def setCor(self, cor):
        self.__Cor = cor
    
    def getCâmbio(self):
        return self.__Câmbio

    def setCâmbio(self, Câmbio):
        self.__Câmbio = Câmbio

    def toDict(self):
        return {
            'Id': self.__Id,
            'Marca': self.__Marca,
            'Modelo': self.__Modelo,
            'Ano': self.__Ano,
            'Cor': self.__Cor,
            'Câmbio': self.__Câmbio
        }

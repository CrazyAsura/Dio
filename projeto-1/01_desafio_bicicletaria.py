class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim plim ...")
    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")
    def correr(self):
        print("Vrummmmm ...")
        
    def __str__(self) -> str:
        return print(f"{self.__class__.__name__}: {", ".join([f"{chave, valor}" for chave, valor in self.__dict__.items()])}")
        
b1 = bicicleta("vermelho", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
b1.__str__()
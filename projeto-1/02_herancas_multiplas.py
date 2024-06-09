class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
       
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)
    
class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

class Cachorro:
    pass

class Leao:
    pass

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
  pass   

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
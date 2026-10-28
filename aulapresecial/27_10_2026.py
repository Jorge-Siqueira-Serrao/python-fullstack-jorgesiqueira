"""
class Carros:
    rodas = 4
    total = 0

    def __init__(self, modelo):
        self.modelo = modelo
        Carros.total += 1

a = Carros("Uno")
b = Carros("Gol")
print(a.rodas, b.rodas, b.total)
b.modelo = "Polo"
print(a.modelo, b.modelo)
"""

"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")

class Cachorro(Animal):
    def latir(self):
        print("Au Au!")

rex = Cachorro("Rex")
print(rex.apresentar())
print(rex.latir())
"""

"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        return "..."

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def som(self):
        return "Miau!"
g = Gato("Mingau", "Cinza")
print(g.nome, g.cor, g.som())
"""

"""
class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def resumo(self):
        n = len(self.musicas)
        return f"{self.nome}: {n} música(s)"

p = Playlist("Rock Clássico")
p.adicionar_musica("Stairway to Heaven")
p.adicionar_musica("Bohemian Rhapsody")
print(p.resumo())
print(p.musicas)
"""
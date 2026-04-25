from abc import ABC, abstractmethod


class Heroi(ABC):
    def __init__(self, nome: str, funcao: str):
        self.nome = nome
        self.funcao = funcao

    @abstractmethod
    def usar_ultimate(self):
        pass

    def __str__(self):
        return f"{self.nome} - Função: {self.funcao}"


class Tanque(Heroi):
    def __init__(self, nome: str):
        super().__init__(nome, "Tanque")

    def usar_ultimate(self):
        print(f"{self.nome}, da função {self.funcao}, usa sua Ultimate para proteger a equipe!")


class Dano(Heroi):
    def __init__(self, nome: str):
        super().__init__(nome, "Dano")

    def usar_ultimate(self):
        print(f"{self.nome}, da função {self.funcao}, usa sua Ultimate para causar grande dano nos inimigos!")


if __name__ == "__main__":
    herois = [
        Tanque("Reinhardt"),
        Dano("Genji"),
        Tanque("D.Va"),
        Dano("Soldier 76")
    ]

    for heroi in herois:
        print(heroi)
        heroi.usar_ultimate()
        print()

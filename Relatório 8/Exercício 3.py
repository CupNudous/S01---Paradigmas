class ArmaCorpoACorpo:
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano

    def __str__(self):
        return f"{self.nome} | Dano: {self.dano}"


class PhantomThieves:
    def __init__(self, nome: str, arma: str):
        self.nome = nome
        self.arma = arma

    def __str__(self):
        return f"Membro: {self.nome} | Arma: {self.arma}"


class Joker:
    def __init__(self, membros: list[PhantomThieves]):
        # Composição: a arma do Joker é criada dentro da própria classe Joker.
        self.arma = ArmaCorpoACorpo("Faca do Joker", 35)

        # Agregação: os membros existem fora da classe Joker e são apenas recebidos.
        self.membros = membros

    def mostrar_equipe(self):
        print("Equipe dos Phantom Thieves")
        print(f"Arma do Joker: {self.arma}")
        print()

        print("Membros da equipe:")
        for membro in self.membros:
            print(membro)


if __name__ == "__main__":
    membro1 = PhantomThieves("Morgana", "Espada Curta")
    membro2 = PhantomThieves("Ryuji", "Cano de Ferro")
    membro3 = PhantomThieves("Ann", "Chicote")
    membro4 = PhantomThieves("Yusuke", "Katana")

    equipe = [membro1, membro2, membro3, membro4]

    joker = Joker(equipe)
    joker.mostrar_equipe()

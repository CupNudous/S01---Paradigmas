from abc import ABC, abstractmethod


class Cibernetico(ABC):
    @abstractmethod
    def realizar_hack(self):
        pass


class Implante:
    def __init__(self, custo: float, funcao: str):
        self.custo = custo
        self.funcao = funcao

    def __str__(self):
        return f"Implante com função '{self.funcao}' e custo de {self.custo:.2f} créditos"


class NetRunner(Cibernetico):
    def __init__(self, nome: str, custo_implante: float, funcao_implante: str):
        self.nome = nome

        # Composição: o Implante é criado e gerenciado pelo próprio NetRunner.
        self.implante = Implante(custo_implante, funcao_implante)

    def realizar_hack(self):
        print(
            f"{self.nome} está realizando um hack usando seu implante: "
            f"{self.implante.funcao}."
        )

    def __str__(self):
        return f"NetRunner: {self.nome} | {self.implante}"


class Faccao:
    def __init__(self, nome: str, membros: list[Cibernetico]):
        self.nome = nome

        # Agregação: a facção recebe objetos cibernéticos já existentes.
        self.membros = membros

    def adicionar_membro(self, membro: Cibernetico):
        self.membros.append(membro)

    def executar_hacks(self):
        print(f"Facção {self.nome} ordenando todos os membros a realizarem hacks:")
        print()

        for membro in self.membros:
            membro.realizar_hack()


if __name__ == "__main__":
    netrunner1 = NetRunner("V", 15000, "Invasão de sistemas corporativos")
    netrunner2 = NetRunner("Alt", 30000, "Quebra de ICE")
    netrunner3 = NetRunner("Spider Murphy", 22000, "Controle remoto de dispositivos")

    faccao = Faccao("Ghosts of Night City", [netrunner1, netrunner2])

    faccao.adicionar_membro(netrunner3)

    print(netrunner1)
    print(netrunner2)
    print(netrunner3)
    print()

    faccao.executar_hacks()

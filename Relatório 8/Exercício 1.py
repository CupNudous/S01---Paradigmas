class Personagem:
    def __init__(self, vida: int, resistencia: int):
        self._vida = vida
        self._resistencia = resistencia

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, nova_vida):
        if not isinstance(nova_vida, int):
            raise TypeError("A vida deve ser um número inteiro.")

        if nova_vida < 0:
            self._vida = 0
        else:
            self._vida = nova_vida

    @property
    def resistencia(self):
        return self._resistencia

    @resistencia.setter
    def resistencia(self, nova_resistencia):
        if not isinstance(nova_resistencia, int):
            raise TypeError("A resistência deve ser um número inteiro.")

        if nova_resistencia < 0:
            self._resistencia = 0
        else:
            self._resistencia = nova_resistencia

    def __str__(self):
        return f"Personagem com {self._vida} de vida e {self._resistencia} de resistência."


class Cavaleiro(Personagem):
    def __init__(self, vida: int, resistencia: int, armadura_pesada: bool):
        super().__init__(vida, resistencia)
        self.armadura_pesada = armadura_pesada

    def __str__(self):
        status_armadura = "possui armadura pesada" if self.armadura_pesada else "não possui armadura pesada"
        return (
            f"Cavaleiro com {self._vida} de vida, "
            f"{self._resistencia} de resistência e {status_armadura}."
        )


if __name__ == "__main__":
    personagem = Personagem(100, 50)
    cavaleiro = Cavaleiro(150, 80, True)

    print(personagem)
    print(cavaleiro)

    cavaleiro.vida = 120
    print(f"Vida atualizada do cavaleiro: {cavaleiro.vida}")

    cavaleiro.vida = -30
    print(f"Vida após receber dano fatal: {cavaleiro.vida}")

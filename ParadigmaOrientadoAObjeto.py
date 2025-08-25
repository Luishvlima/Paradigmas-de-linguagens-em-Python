#Soma dos números de 1 a 10:
class Somador:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def calcular_soma(self):
        soma = 0
        for i in range(self.inicio, self.fim + 1):
            soma += i
        return soma

somador = Somador(1, 10)
resultado = somador.calcular_soma()
print(f"A soma dos números de 1 a 10 é: {resultado}")
#Luis Henrique Vieira Lima
#Soma dos números de 1 a 10:
def calcular_soma(inicio, fim):
    soma = 0
    for i in range(inicio, fim + 1):
        soma += i
    return soma
resultado = calcular_soma(1, 10)
print(f"A soma dos números de 1 a 10 é: {resultado}")
#Luis Henrique Vieira Lima
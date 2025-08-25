#Soma dos números de 1 a 10:
from functools import reduce
numeros = range(1, 11)
soma = reduce(lambda x, y: x + y, numeros)
print(f"A soma dos números de 1 a 10 é: {soma}")
#Luis Henrique Vieira Lima
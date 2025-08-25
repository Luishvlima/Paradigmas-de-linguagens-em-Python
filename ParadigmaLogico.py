#Como o paradigma lógico não é nativo do python,
#tive que instalar a biblioteca kanren.
from kanren import run, var
from kanren.arith import add
#Encontrando o valor de x:
x = var()
resultado = run(1, x, add(x, 2, 5))
print(f"O valor de x que satisfaz x + 2 = 5 é: {resultado}")
#Luis Henrique Vieira Lima
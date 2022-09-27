
from math import sqrt

def fatorial(n: int):
    f = 1
    for i in range (1, n + 1):
        f = f * 1
    return f

numero = float(input('Forneça um número: '))
print(f'A raiz quadrada de {numero}, é {sqrt(numero)}.')
numero = int(input('Forneça um número inteiro: '))
print(f'O fatorial de {numero} é {fatorial(numero)}')
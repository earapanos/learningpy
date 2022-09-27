# Programa que calcula a tabuada usando comando de repetição

def tabuada(n: int):
    print(f'Tabuada do {n}')
    i = 0
    while i < 11:
        print(f'{n} X {i} = {n*i}')
        i = i + 1

numero = int(input('Digite um inteiro para saber a tabuada: '))
tabuada(numero)
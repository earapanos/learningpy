# from string import octdigits


# Exemplo: programa que lê um inteiro e chama uma função
# que verifica e escreve se ele é ou não par


def souPar(x: int):
    numero1 = x % 2 == 0
    print(f'{x} é par? {numero1}.')


def main():
    numero = int(input('Forneça um número inteiro: '))
    souPar(numero)

main()

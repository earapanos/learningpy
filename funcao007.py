# Exemplo : programa que lê um inteiro e chama uma função que verifica 
# se ele é ou não par setando a variável global

def soupar(x: int):
    global par
    par = (x % 2 == 0)


def main():
    numero = int(input('Forneça um número inteiro: '))
    soupar(numero)
    if par:
        print(f'{numero} é par.')
    else:
        print(f'{numero} é ímpar.')

par = False  #global 
main()
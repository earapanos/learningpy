# Exemplo: um programa que lê um n inteiro e chama uma função
# que verifica e escreve se ele é ou não par

def souPar():
    numero1 = numero % 2 == 0
    print(f'{numero} é par? {numero1}')
    

numero = int(input('Forneça um número inteiro: '))
souPar()
print('Adeus!')
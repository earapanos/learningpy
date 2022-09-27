# Exemplo: um programa que lê um inteiro e chama a função que 
# verifica se ele é ou não par retornando o resultado

# QUANDO A FUNÇÃO TEM RETORNO, A CHAMADA DA FUNÇÃO TEM SAÍDA PELA FUNÇÃO RETORNADADA

def soupar(x: int):
    saida = (x % 2 == 0)
    return saida

def main():
    numero = int(input('Forneça um inteiro: '))
    if soupar(numero):  # if soupar(true):
        print(f'{numero} é par.')
    else:  #else soupar(false):
        print(f'{numero} é ímpar.')
        
main()
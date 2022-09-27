# Uso do comando de repetição While.
# Programa que calcula o peso em Kg de minério em uma determinada amostra

def teor_minerio(n: int):
    amostra = 1
    while amostra <= n:
        nome_amostra = input('Entre com o nome do minério:\n')
        print('Entre com o peso do minério bruto (kg):')
        n1 = float(input())
        print(f'Entre com o teor de {nome_amostra} (%):')
        n2 = float(input())
        peso_minerio = (n1*n2) / 100 
        print(f'A quantidade de {nome_amostra} em {n1:.3f}(kg) de minério bruto é: {peso_minerio:.3f}(kg).\n')
        amostra = amostra + 1

quantidade = int(input('Digite a quantidade de amostras que você tem: '))
teor_minerio(quantidade)


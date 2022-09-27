# Uso do comando de repetição WHILE.

def main():
    quantidade_alunos = 1
    while quantidade_alunos < 4:
        nome = input('Entre com o nome do aluno: \n')
        print('Entre com as 3 notas de {}'.format(nome))
        n1 = float(input())
        n2 = float(input())
        n3 = float(input())
        MH = n1*0.2 + n2*0.35 + n3*0.45
        print(f'A média harmônica ponderada de {nome} é: {MH:.2f}.')
        quantidade_alunos = quantidade_alunos + 1


main()
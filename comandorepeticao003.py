def main(n: int):
    quantidade_alunos = 1
    somaMH = 0
    while quantidade_alunos <= n:
        nome = input('Entre com o nome do aluno: \n')
        print('Entre com as 3 notas de {}'.format(nome))
        n1 = float(input())
        n2 = float(input())
        n3 = float(input())
        MH = n1*0.2 + n2*0.35 + n3*0.45
        somaMH = somaMH + MH
        print('A média harmônica ponderada de {} é: {}.'.format(nome, MH))
        quantidade_alunos = quantidade_alunos + 1
    media_turma = somaMH / n
    print('A média da turma é: {}.'.format(media_turma))    


nro_estudantes = int(input('Forneça o tamanho da turma: '))


main(nro_estudantes)
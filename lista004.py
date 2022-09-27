notas = []
alunos = []

def entrada_dados():
    novo_nome = input('Digite o nome do aluno: ')
    nova_nota = float(input('Digite a nota: '))
    alunos.append(novo_nome)
    notas.append(nova_nota)

def programa_principal():
    while True:           # esse comando vai fazer preencher pra sempre a lista
        entrada_dados()
        
        for i in range(len(notas)):
            print(f'Aluno: {alunos[i]}')
            print(f'Nota: {notas[i]}')
        print('+++++++++++++++++')

        finalizar = input('Deseja finalizar? (s/n)')
        if finalizar == 's':
            break




programa_principal()
# Listas. Exemplo: guardar as notas das provas de qualquer quantidade de alunos.


notas = [7.0, 5.0, 10]
alunos = ['Jean', 'Yan', 'Eduardo']

nova_nota = float(input('Digite a nota: '))
novo_nome = input('Digite o nome: ')

notas.append(nova_nota)
alunos.append(novo_nome)

                             #len le o 
for i in range(len(notas)):  # Range, função em py que retorna sequencia de valores
    print(i)                    # i é a atribuição de um índice
    print(f'Aluno: {alunos[i]}')
    print(f'Notas: {notas[i]}')
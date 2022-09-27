#Listas. Exemplo: Guardar as notas das provas de qualquer quantidades de alunos.

provas = [5.5, 6.5, 7.5, 8.0, 9.5, 7.0, 9.0]
nota = float(input('Entre com a nota: '))
provas.append(nota)   # Adiciona novo item na lista

for nota in provas:
    print(nota)
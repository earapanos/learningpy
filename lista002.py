# Listas. Exemplo: guardar as notas das provas de qualquer quantidade de alunos.

notas = [7.0, 8.0, 9.85]

nova_nota = float(input('Digite a nota: '))
notas.append(nova_nota)

print(notas)

for notas in notas:  # Oganiza na vertical o resultado;
    print(f'Nota = {notas:^20}')
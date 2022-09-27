

contaAluno = 0
acumNota = 0
while contaAluno < 10:
    nota = float(input('Entre com a nota: '))
    acumNota = acumNota + nota
    contaAluno = contaAluno + 1
media = acumNota / 10
print(f'A média da turma é {media}.')
valores = []
valores.append(8)
valores.append(0)
valores.append(7)

for v in valores:
    print(f'{v}...', end='')  # adiciona lado a lado os valores

    print('\n')

valores = []
valores.append(8)
valores.append(0)
valores.append(7)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
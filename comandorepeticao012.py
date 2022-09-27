# Comando de repetição usando laços aninhados

def tabuada():
    j = 2
    while j <= 9:
        print(f'Tabuada do {j}.')
        i = 1 
        while i <= 10:
            print(f'{j} x {i} = {j * i}')
            i = i + 1
        print('-' * 15)
        j = j + 1

tabuada()
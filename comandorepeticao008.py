# Cálculo de fatorial usando comandos de repetição

def fatorial(n:int):
    if n <= 1:
        return 1
    f = 1
    i = 2
    while i <= n:
        f = f * i
        i = i + 1
    return f 

num = int(input('Forneça um inteiro: '))
print(f'{str(num)}! = {str(fatorial(num))}')


def fatorial(n:int):
    if n <= 1:
        return 1
    f = 1
    for i in range (1, n+1, 1):
        f = f * i
    return f
    

variavel = int(input('Entre com um inteiro: '))
fatorial(variavel)
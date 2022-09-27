from re import I


def fatorianl(n: int):
    if n <= 1:
        return 1
    f = 1
    i = 2
    while i <= n:
        f = f * i
        i = i + 1
    return f


num = int(input('Forneça um inteiro: '))
print( '{}! = {}'.format(num, fatorianl(num)))
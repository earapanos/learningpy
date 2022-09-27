# exemplo: função que recebe 3 numeroes e retorna o maior deles

def maior3(x: float, y: float, z:float):
    maximo = x
    if y > maximo:
        maximo = y
    if z > maximo:
        maximo = z 
    return maximo 

def main():
    a = float(input('Digite um número: '))
    b = float(input('Digite um número: '))
    c = float(input('Digite um número: '))
    print(f'O maior número entre {a, b, c} é: {maior3(a, b, c)}.')


main()
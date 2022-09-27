from math import trunc

def main():
    print('Entre com um número:')
    x = float(input())
    print('Entre com um número:')
    y = float(input())
    z = x + y
    print(f'{x} + {y} = {trunc(z)}')

main()

print('Tchau!')
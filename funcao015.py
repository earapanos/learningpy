def souPar(x: int):
    print(x, 'é par?', número % 2 == 0)

def main():
    número = int(input('Forneça um inteiro: '))
    souPar(número)

main()
print('Tchau')
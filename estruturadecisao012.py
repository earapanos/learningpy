lado1 = float(input('Forneça o lado 1 do triângulo: '))
lado2 = float(input('Forneça o lado 2 do triângulo: '))
lado3 = float(input('Forneça o lado 3 do triângulo: '))
if lado1 == lado2 == lado3:
    print('O triângulo é equilátero.')
elif lado1 != lado2 != lado3:
    print('O triângulo é escaleno.')
else:
    print('O triângulo é isósceles')
input('Digite <enter> para encerrar.')

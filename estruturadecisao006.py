print('Este programa verifica se o triângulo é equilátero, isósceles ou escaleno.')
lado1 = float(input('Forneça o lado 1 do triângulo '))
lado2 = float(input('Forneça o lado 2 do triângulo '))
lado3 = float(input('Forneça o lado 3 do triângulo '))
if lado1 == lado2 and lado2 == lado3:
    print('O triângulo é equilátero.')
if lado1 != lado2 and lado1 != lado3 and lado3:
    print('O triângulo é escaleno.')
if (lado1 == lado2 and lado2 != lado3) or\
   (lado2 == lado3 and lado2 != lado3) or\
   (lado3 == lado2 and lado2 != lado1):
    print('O triângulo é isósceles.')

# K = C + 273.15
# C = (F-32)/1.8
# F = 1.8*(K - 273.15)+32

temperatura = float(input('Forneça a temperatura de entrada'))
unitIn = input('Forneça medidade de entrada (K ou C)').upper() # Converte para maiúsculas
unitOut = input('Forneça medida de saída (K ou C; deve ser diverente da de entrada)').upper()
unitIn = unitIn.upper() # Converte para maiúsculas
unitOut = unitOut.upper() # Converte para maiúsculas
if unitIn == 'C':
    if unitOut == 'K':
        print(temperatura + 273.15)
    elif unitOut == 'F':
        print(temperatura*1.8 + 32)

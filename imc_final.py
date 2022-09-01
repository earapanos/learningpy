print('{:^100}'.format('Olá tudo bem?'))
print('{:^100}'.format('Este programa foi criado para realizar o Cálculo do Índice de Massa Corporal (IMC).'))
print('{:^100}'.format('O cálculo é feito a partir da fórmula: PESO/ALTURA^2.'))
print('\n')
altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em kilogramas: '))
imc = float(peso/(altura*altura))
if ((imc)) < 18.5:
    print('Seu IMC é: ''{:.2f}'.format(imc))
    print('Você está abaixo do peso segundo a OMS.')
elif (((imc)) >= 18.5 and ((imc)) < 24.9):
    print('Seu IMC é: ''{:.2f}'.format(imc))
    print('Você está com o peso normal segundo a OMS.')
elif (((imc)) >= 24.9 and ((imc)) < 29.9):
    print('Seu IMC é: ''{:.2f}'.format(imc))
    print('Você está com excesso de peso segundo a OMS.')
elif (((imc)) >= 29.9 and ((imc)) < 34.9):
    print('Seu IMC é: ''{:.2f}'.format(imc))
    print('Você está com obesidade classe I segundo a OMS.')
elif (((imc)) >= 34.9 and ((imc)) < 39.9):
    print('Seu IMC é: ''{:.2f}'.format(imc))
    print('Você está com obesidade classe II segundo a OMS.')
elif (((imc)) >= 39.9):
    print('Seu IMC é: ''{:.2f}'.format(imc))
    print('Você está com obesidade classe III segundo a OMS.')
print('\n')
input('Digite <enter> para encerrar.')

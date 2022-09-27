# programa que lê o nome  cpf fazendo a consistência de entrada

erro = True
while erro:
    nome = input('Forneça o nome: ')
    palavras = nome.split(' ')
    erro = False
    for palavra in palavras:
        if not palavra.isalpha(): # só letras?
            print('Só deve conter letras e espaços')
            erro = True
            break
print(nome.title())

while True:
    cpf = input('Forneça o CPF (só números): ')
    if cpf.isdecimal() and len(cpf) == 11:
        break
    print('Só deve conter números (11)')
print(cpf)
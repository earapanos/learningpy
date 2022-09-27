# Variáveis globais, locais e escopo

def mudaX():
    x = 5 # x local
    print(f'X aqui é local e vale {x}.')

x = 7 #x global
mudaX()
print(f'X é global e fale {x}.')
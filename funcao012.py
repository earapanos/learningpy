def mudaX():
    x = 5 # x local
    print('x aqui é local e vale ', x)

x = 7 #x é global
mudaX()
print('x é global e vale ', x)
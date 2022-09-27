from re import X


def mudaX():
    global x 
    x = 5 # global
    print('x é global no programa e vale ', x)

x = 7 
mudaX()
print('x é global e vale ', x)
# método de apagar elementos da lista

lanche = ['pão', 'alface', 'cebola roxa', 'cogumelo', 'hommus']
del lanche[1] 

print(lanche)

# método pop - normalmente usado para eliminar o último elemento

lanche = ['pão', 'alface', 'cebola roxa', 'cogumelo', 'hommus']
lanche.pop(2)

print(lanche)

# método remove - você indica o valor que você quer tirar ao invés do índice

lanche = ['pão', 'alface', 'cebola roxa', 'cogumelo', 'hommus']
lanche.remove('cogumelo') 

print(lanche)
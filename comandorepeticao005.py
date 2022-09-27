def tabuada():
    j = 2
    while j <= 9:
        i = 0
        print(f'Tabuada do {j}: \n')
        while i <= 10:
            print('{} X {} = {}'.format(j, i, j*i))
            i = i + 1
        print('-'*30)
        j = j + 1


tabuada()

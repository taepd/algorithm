n = '75254'

for i in range(len(n), 0, -1):
    # print(f'[{n[-i]+"0"*(i-1)}]')
    print([int(n[-i])*10**(i-1)])
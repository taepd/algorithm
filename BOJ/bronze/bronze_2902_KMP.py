print(''.join([e[0] for e in input().split('-')]))

print(*([e[0] for e in input().split('-')]), sep='')

print(*filter(str.isupper, input()), sep="")


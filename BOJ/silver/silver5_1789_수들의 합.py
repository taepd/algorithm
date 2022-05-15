n = int(input())

k = int((n*2)**0.5)

s = (k*(k+1))/2

if n >= s:
    print(k)
else:
    print(k-1)
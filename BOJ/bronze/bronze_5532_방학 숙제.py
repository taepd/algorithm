lst = []
for __ in range(5):
    lst.append(int(input()))
L, A, B, C, D = lst

print(L - max((A-1)//C+1, (B-1)//D+1))



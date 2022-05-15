
n = int(input())
ans = 0
for i in range(1, n):
    ans += (n+1)*i
print(ans)

# 위는 결국 시그마 합이므로

n=int(input())
print((n+1)*n*(n-1)//2)
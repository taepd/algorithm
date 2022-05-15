
h, m = map(int, input().split())

n = int(input())

ans = (h*60)+m+n

if ans >= 60*24:
    print((ans//60)%24, ans%60)
else:
    print(ans//60, ans%60)

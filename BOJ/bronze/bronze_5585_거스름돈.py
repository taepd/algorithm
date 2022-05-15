"""
가장 큰 화폐단위부터 greed
"""

n = int(input())
total = 1000 - n
unit = [500, 100, 50, 10, 5, 1]
ans = 0
for u in unit:
    ans += total // u
    total = total % u

print(ans)
# l, m, n = map(int, input().split())
#
# if l == m == n:
#     ans = 10000 + l * 1000
# elif l != m != n != l:
#     ans = max(l, m, n) * 100
# else:
#     ans = 1000 + n * 100 if l ^ m else 1000 + l * 100
#
# print(ans)

l, m, n = map(int, input().split())
print(10000 + l * 1000 if l == m == n else max(l, m, n) * 100 if l != m != n != l else 1000 + n * 100 if l ^ m else 1000 + l * 100)

#
# n = int(input())
#
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
#
# arr1.sort()
#
# tpl2 = [(i, v) for i, v in enumerate(arr2)]
# tpl2.sort(key=lambda x: x[1], reverse=True)
#
# print(sum(map(lambda x: x[0]*x[1], zip(arr1, [e[1] for e in tpl2]))))

# 리스트가 필요없고 단순 계산만 필요하니 간단하게 가능
n = int(input())

arr1 = sorted(map(int, input().split()))
arr2 = sorted(map(int, input().split()), reverse=True)

print(sum(arr1[i]*arr2[i] for i in range(n)))

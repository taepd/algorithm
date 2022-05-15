# import sys
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
#
# arr = [int(input()) for __ in range(n)]
#
# arr.sort()
#
#
# # 최대 거리 s로 공유기를 설치할 수 있는지 여부
# def f(s):
#     tmp = k - 1  # 첫 번째 집에 공유기 설치한 것 반영
#     house = arr[0]
#     for i in range(len(arr)-1):
#         if arr[i+1] - house >= s:
#             tmp -= 1
#             house = arr[i+1]
#     if tmp <= 0:
#         return True
#     else:
#         return False
#
# # arr 길이만큼 이분 탐색
# start, end = 0, arr[-1]-1  # 두 집 사이의 거리 값이므로 -1
# while start <= end:
#     mid = (start + end) // 2
#     if f(mid):
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(end)  # end로 해야 계산이 제대로 됨;

import sys

def sol2110():
    # n, c, *house = map(int, sys.stdin.read().split())
    input = sys.stdin.readline

    n, c = map(int, input().split())

    house = []

    for __ in range(n):
        house.append(int(input()))

    house.sort()
    s, e = 1, (house[-1] - house[0]) // c + 1
    while s <= e:
        m = (s + e) // 2
        cnt, prev = 1, house[0] + m
        for h in house[1:]:
            if h >= prev:
                cnt, prev = cnt + 1, h + m
        s, e = (m + 1, e) if cnt >= c else (s, m - 1)
    print(e)


if __name__ == '__main__':
    sol2110()


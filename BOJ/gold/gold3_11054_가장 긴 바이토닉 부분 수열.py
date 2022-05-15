
'''
가장 긴 부분수열의 길이 함수를 이용해
특정 인덱스를 기준으로 증가하는 수열, 감소하는 수열(reversed)에 대해 각각 구하고
이를 더하는 전략
brute force라서 시간 효율성이 너무 떨어짐  4188ms
'''
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# seq = list(map(int, input().split()))
#
# def make_sub_seq(arr):
#     lis = [arr[0]]
#     for num in arr[1:]:
#         if num > lis[-1]:
#             lis.append(num)
#         else:
#             for i in range(len(lis)):
#                 if lis[i] >= num:
#                     lis[i] = num
#                     break
#     return len(lis)
#
# longest_bitonic = 0
#
# for i in range(len(seq)):
#     forward_arr = seq[:i+1]
#     backward_arr = seq[i:][::-1]
#     longest_bitonic = max(longest_bitonic, make_sub_seq(forward_arr)+make_sub_seq(backward_arr)-1)
#
# print(longest_bitonic)

'''
bisect를 이용하는 방법
dp에 각 index 마다 lis, 즉 가장 긴 부분수열의 길이-1(정확히는 index)를 저장해서
연산 속도 향상
'''
import sys
import bisect

input = sys.stdin.readline
n = int(input())

def make_lis_len(arr):
    LIS = [arr[0]]
    dp = [0] # 해당 index까지의 가장 긴 부분수열의 길이-1(정확히는 index)를 저장
    for i in range(1, n):
        idx = bisect.bisect_left(LIS, arr[i])
        dp.append(idx)
        if(idx == len(LIS)):
            LIS.append(arr[i])
        else:
            LIS[idx] = arr[i]
    return dp

arr = list(map(int, input().split()))
LIS = make_lis_len(arr)
LDS = make_lis_len(arr[::-1])[::-1]
print(max([LIS[i] + LDS[i] + 1 for i in range(n)]))


"""
combination을 이용한 brute force -> 시간 초과
"""

# from itertools import combinations
#
# N, M, L = map(int, input().split())
#
# cut_point_lst = [int(input()) for i in range(M)]
#
# for _ in range(N):
#     s = int(input())
#     combo_lst = combinations(cut_point_lst, s)
#     max_len = 0
#
#     for combo in combo_lst:
#         min_len = float('inf')
#         for i, v in enumerate(combo):
#             if len(combo) == 1:
#                 candidate = min(v, L-v)
#             else:
#                 if i == 0:
#                     candidate = v
#                 elif i == s - 1:
#                     candidate = min(L-v, combo[i] - combo[i-1])
#                 else:
#                     candidate = combo[i] - combo[i-1]
#             min_len = min(min_len, candidate)
#         max_len = max(max_len, min_len)
#
#     print(max_len)

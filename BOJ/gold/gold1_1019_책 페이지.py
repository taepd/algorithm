
# start, end = map(int, input().split())
# decimal_arr = [0 for _ in range(10)]
#
# def count_page(start, end):
#     for i in range(start, end+1):
#         tmp = str(i)
#         for j in tmp:
#             decimal_arr[int(j)] += 1
#
#     print(*decimal_arr)
#
# 
# count_page(start, end)

# def sigma_ratio(n):
#     return ((10**n)-1)/(10-1)
#
n = input()
decimal_arr = [0 for _ in range(10)]

for i in range(len(n)):  # 1의 자리부터 올라가며
    m = i+1  # 자릿수
    target = n[-m:]  # 현재 해결할 숫자 string
    if m == 1:  # 1자리인 경우
        for j in range(1, int(target)+1):
            decimal_arr[j] += 1
    else:
        # target: 35
        first_number = int(target[0])  # 이번 순회에서 해결하는 첫 번째 숫자
        second_number = int(target[1])
        second_to_end = int(target[1:])
        for k in range(10):  # 모든 자릿수에 더함
            if k == 0 and second_number == 0:
                if i == 1:
                    decimal_arr[k] += 1
                decimal_arr[k] += first_number*(m-1)*(10**(m-2))-(10**(i-1))
            else:
                decimal_arr[k] += first_number*(m-1)*(10**(m-2))  # 공통으로 모든 자릿수 커지는 수
        for l in range(1, first_number):  # 첫 번째 숫자 이하인 것만 반영
            decimal_arr[l] += 10**(m-1)
        decimal_arr[first_number] += second_to_end+1  # 두 번째 숫자 바로 직전만 반영


print(*decimal_arr)








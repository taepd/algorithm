import math

"""
n : 노래의 개수
l : 노래의 길이
c : 한 시디의 용량
"""
n = int(input())
l = int(input())
c = int(input())


# 한 cd당 담을 수 있는 곡의 개수
q = (c+1) // (l+1)

# 한 cd당 노래의 개수가 13의 배수이면 -1
if q % 13 == 0:
    q -= 1

# 필요한 cd 개수
ans = math.ceil(n / q)

# 자투리 곡수
r2 = n % q
# 자투리 곡수로 만든 cd의 수록곡이 13의 배수인 경우
if r2 and r2 % 13 == 0:
    if ans == 1:
        ans += 1
    else:
        # 마지막 cd의 추가 곡에 대한 캐퍼가 있으면
        while (r2 + 1) * (l + 1) - 1 <= c:
            r2 += 1
            q -= 1
            # 다른 cd도 13의 배수가 되는지 체크
            if q % 13 != 0:
                break
        else:
            ans += 1

print(ans)

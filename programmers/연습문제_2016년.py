"""
문제 설명
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
입출력 예
a	b	result
5	24	TUE
"""

def solution(a, b):

    month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_count = 0
    for i in range(a-1):
        day_count += month_list[i]
    day_count += b
    day_of_week = day_count % 7

    if day_of_week == 1: return 'FRI'
    elif day_of_week == 2: return 'SAT'
    elif day_of_week == 3: return 'SUN'
    elif day_of_week == 4: return 'MON'
    elif day_of_week == 5: return 'TUE'
    elif day_of_week == 6: return 'WED'
    elif day_of_week == 0: return 'THU'

print(solution(2, 28))

"""
간결한 풀이
"""

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))

"""
datatime 함수 활용
"""

import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]


#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))

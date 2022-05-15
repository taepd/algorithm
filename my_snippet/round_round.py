# 0.5 단위 반올림

from math import floor


def round_round(n):
    quotient = floor(2*n)*0.5
    remainder = round((n-quotient)*2)*0.5
    return quotient + remainder


print(round_round(3.76))


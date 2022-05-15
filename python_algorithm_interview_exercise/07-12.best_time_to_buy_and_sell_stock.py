"""
한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
prices = [7,1,5,3,6,4]

# brute force
# timeout으로 실패
from typing import List


def maxProfit(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# 저점과 현재 값과의 차이 계산
# 최대 이익은 결국 최솟값과 최댓값의 차이므로,
# 저점을 갱신하면서 현재값과 저점간의 차이로 최대 이익을 갱신하는 전략
# 64ms
import sys

def mayProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

print(mayProfit(prices))



"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	69668	21067	13740	29.839%
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1
1
1
0
0
1
"""

"""
이진 탐색 bisect 라이브러리를 활용한 풀이
"""

import sys
from bisect import bisect
input = sys.stdin.readline

n = int(input().rstrip())
arr1 = sorted(map(int, input().rstrip().split()))
m = int(input().rstrip())
arr2 = map(int, input().rstrip().split())

for e in arr2:
    print(1) if arr1[bisect(arr1, e)-1] == e else print(0)

"""
이진 탐색을 구현한 풀이
"""

from sys import stdin
n = stdin.readline()
arr1 = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
arr2 = map(int, stdin.readline().split())

def binary(e, arr, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if e == arr1[m]:
        return 1
    elif e < arr1[m]:
        return binary(e, arr1, start, m-1)
    else:
        return binary(e, arr1, m+1, end)

for e in arr2:
    start = 0
    end = len(arr1)-1
    print(binary(e,arr1,start,end))


"""
set의 원소 찾기는 O(1)인 것을 활용한 풀이
"""

from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')
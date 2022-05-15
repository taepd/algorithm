"""
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]
입출력 예 설명
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.
"""

def solution(n, m):
    gcd, lcm = 0, 0  # 초기화
    l, h = min(n, m), max(n, m)  # 큰 수와 작은 수를 구분
    d_list = [i for i in range(1, l//2+1) if l%i ==0] + [l]  # 작은 수의 약수 리스트
    for c in d_list:  # 큰 수를 작은 수 약수로 나누어 최대공약수 구함
        if h % c == 0:
            gcd = max(gcd, c)
    lcm = n*m/gcd

    return [gcd, lcm]


"""
유클리드 호제법을 이용한 풀이
"""
def solution(n, m):
    a, b = max(n, m), min(n, m)  # 굳이 없어도 되는듯?
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
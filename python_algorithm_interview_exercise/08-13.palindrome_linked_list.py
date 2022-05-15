"""
연결 리스트가 팰린드롬 구조인지 판별하라.
Given a singly linked list, determine if it is a palindrome.
Input: 1->2
Output: false

Input: 1->2->2->1
Output: true
"""

# 리스트 변환
# 파이썬 리스트는 특정 인덱스에 대한 pop()도 지원함
# 파이썬 리스트로 변환해서 풀이
# 164ms
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))


def isPalindrome(head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

# deque를 이용한 최적화
# q.pop(0)는 첫 번째 값을 꺼낼 때 모든 값이 한 칸씩 shifting되며, O(n)이 소요됨
# deque는 양방향 모두 O(1)이 소요
# 72ms

import collections
from typing import Deque


def isPalindrome(head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

# 런너를 이용한 우아한 풀이
# 런너기법과 다중할당 트랜잭션 활용
# 64ms

def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next  # 다중할당 트랜잭션 처리
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


print(isPalindrome(head))




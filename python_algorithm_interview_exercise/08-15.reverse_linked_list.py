"""
연결 리스트를 뒤집어라.
Reverse a singly linked list.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# 재귀 구조로 뒤집기
# 현재 node.next를 prev로 연결해주는 것이 핵심
# 40ms

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

# 반복 구조로 뒤집기
# 재귀와 기본 전략은 같음
# 시간/공간 복잡도가 조금 더 낮음
# 32ms

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

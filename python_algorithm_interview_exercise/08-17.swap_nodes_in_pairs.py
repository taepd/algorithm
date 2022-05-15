"""
연결 리스트를 입력받아 페어 단위로 스왑하라

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]
"""

# 값만 교환
# 실제론 금지된 풀이법
# 24ms

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

# 반복 구조로 스왑
# 스왑할 경우 연결도 새로 맺어줘야 해서 까다롭다
# 20ms

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록
            prev.next = b

            # 다음 번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next  # head를 가리키는 node가 바뀌기 때문에 그 이전 값을 root로 설정해서 root.next 리턴


# 재귀 구조로 스왑
# 반복 구조보다 깔끔하다
# 다시 볼 것
# 20ms

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

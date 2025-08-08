# https://leetcode.com/problems/reverse-linked-list/

"""
解説:
・時間計算量: O(n)
・空間計算量: O(1)
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        reversed_head = None

        curr = head
        next = None
        
        while curr:
            next = curr.next
            curr.next = reversed_head
            reversed_head = curr
            curr = next
        
        return reversed_head
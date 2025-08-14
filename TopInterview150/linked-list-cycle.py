# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False
        
        currents = []
        while head:
            currents.append(head)
            if head.next == None:
                return False
            if head.next in currents:
                return True

            head = head.next
        
        return False


class CorrectSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's Cycle Detection Algorithm (Two Pointers / Tortoise and Hare)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return False
        
        # Initialize slow and fast pointers
        slow = head
        fast = head.next
        
        # Move pointers at different speeds
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
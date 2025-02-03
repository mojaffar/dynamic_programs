# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from dynamic_programs.merge_two_sorted_linked_list import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            # save pointers
            nextPairs = curr.next.next
            second = curr.next

            # swap the nodes
            second.next = curr
            curr.next = nextPairs
            prev.next = second

            # update the pointers
            prev = curr
            curr = nextPairs

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpointer, fastpointer = head, head

        while fastpointer and fastpointer.next:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next
            if fastpointer == slowpointer:
                return True
        return False


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # curr = head
        # listVal = []

        # while curr:
        #     listVal.append(curr.val)
        #     curr = curr.next

        # return listVal == listVal[::-1]
        
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Step 3: Compare both halves
        left, right = head, prev
        while right:  # right half might be shorter in odd-length list
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
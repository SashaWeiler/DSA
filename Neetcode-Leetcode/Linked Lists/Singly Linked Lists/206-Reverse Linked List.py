def reverseList(self, head):
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# My solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            nextPointer = cur.next
            if nextPointer is None:
                break
            cur.next = prev
            # Was using cur.val which was causing issues
            prev = cur
            cur = nextPointer
        return prev

# Recursive solution

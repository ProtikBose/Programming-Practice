class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print(head.next.val)
        print(head.val)

        if not head or not head.next:
            print(head.val)
            return
        
        temp = head.next
        head.next = head
        head.next = temp 
        self.swapPairs(head.next)
        #print(head.next.val)
        #print(head.val)

sol = Solution()
sol.swapPairs(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
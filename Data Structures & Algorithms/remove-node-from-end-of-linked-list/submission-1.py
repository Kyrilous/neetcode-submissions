# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next:
            return None

        count = 0
        curr = head
        while(curr):
            print(curr.val)
            curr = curr.next
            count += 1

        if(n == count):
            return head.next

        curr = head;
        for i in range(count):
            ##We must be at the node before the one to remove
            if i == (count - n - 1):
                print("Stopping at node: ", curr.val)
                curr.next = curr.next.next
                break
            curr = curr.next

        return head





        
       
       
       
       
       
       
       
       
        # if n == 1 and head and head.next:
        #     head = head.next
        # else:
        #     prev = ListNode()
        #     prev.next = head
        #     count = 1
        #     curr = head
        #     while curr.next:
        #         curr = curr.next
        #         prev = prev.next
        #         count += 1
        #         if(count == n):
        #             curr = prev
        #             curr.next = curr.next.next
                

                
            
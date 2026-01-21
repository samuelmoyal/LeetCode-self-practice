# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        init=ListNode()
        init.next=head
        node=head
        n_chain=0 
        prev=node
        while node.next != None:
            prev=node
            node=node.next
            n_chain+=1
        node=init
        for i in range (n_chain-n+1):
            node=node.next
        future=node.next
        if future!=None:
            two_upfront=future.next
            node.next=two_upfront
        return init.next
        
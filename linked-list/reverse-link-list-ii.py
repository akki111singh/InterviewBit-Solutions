# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        head = A
        if B==C:
            return head
        beforeB = None
        prev = None
        curr = A
        n = 1
        Bnode = None
        afterC = None
        while curr:
            if n==B:
                Bnode = curr
                beforeB = prev
                prev = curr
                curr = curr.next
                n+=1
            elif n>B and n<C:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
                n+=1
            elif n==C:
                Cnode = curr
                Bnode.next = curr.next
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
                n+=1
                break
            elif n<B:
                beforeB = curr
                prev = curr
                curr = curr.next
                n+=1
        if beforeB:
            beforeB.next = Cnode
            return head
        else:
            return Cnode
            
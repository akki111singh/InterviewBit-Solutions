# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A.val<B.val:
            head = A
            curr = A
            other = B
        else:
            head = B
            curr = B
            other = A
        while curr.next is not None and other is not None:
            if curr.next.val<other.val:
                curr = curr.next
            else:
                temp = curr.next
                curr.next = other
                curr = other
                other = temp
        if other is not None:
            curr.next = other
        return head
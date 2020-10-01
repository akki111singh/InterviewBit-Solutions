# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        n = 1
        head = A
        curr = head
        while curr.next:
            n+=1
            curr = curr.next
        if n==1:
            return 1
        elif n==2:
            return 1 if A.val==A.next.val else 0
        revhead = n//2 + 1
        i = 1
        curr = head
        while i<revhead:
            curr = curr.next
            i+=1
        prev = None
        nextt = curr.next
        while nextt:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        isPalin = 1
        last = prev
        first = head
        for i in range(n//2):
            if last.val!=first.val:
                isPalin=0
            last = last.next;first = first.next
        return isPalin
        
        
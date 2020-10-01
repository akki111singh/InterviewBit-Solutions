# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        head1 = A
        head2 = B
        head = ListNode((head1.val+head2.val)%10)
        carry = (head1.val+head2.val)//10
        head1 = head1.next
        head2 = head2.next
        curr = head
        while head1 is not None and head2 is not None:
            val = (head1.val+head2.val+carry)%10
            carry = (head1.val+head2.val+carry)//10
            curr.next = ListNode(val)
            curr = curr.next
            head1 = head1.next;head2 = head2.next
        if head1:
            curr.next = ListNode((head1.val+carry)%10)
            carry = (head1.val+carry)//10
            curr = curr.next
            head1 = head1.next
        if head2:
            curr.next = ListNode((head2.val+carry)%10)
            carry = (head2.val+carry)//10
            curr = curr.next
            head2 = head2.next
        if carry>0:
            curr.next = ListNode(carry)
            curr = curr.next
        return head

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def reverse(llist):
    prev = None
    curr = llist

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

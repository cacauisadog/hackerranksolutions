#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def reverse(llist):
    prev = None
    curr = llist

    while curr is not None:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next

    return prev

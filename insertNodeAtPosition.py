#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(llist, data, position):
    head = llist
    cur = llist
    new_node = SinglyLinkedListNode(data)
    i = 0

    if position == 0:
        new_node.next = cur
        return new_node

    while i < position - 1:
        cur = cur.next
        i += 1

    next = cur.next
    cur.next = new_node
    new_node.next = next

    return head

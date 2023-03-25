#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data < head2.data:
        merged_list_head = SinglyLinkedListNode(head1.data)
        head1 = head1.next
    else:
        merged_list_head = SinglyLinkedListNode(head2.data)
        head2 = head2.next

    cur = merged_list_head
    h1 = head1
    h2 = head2

    while True:
        if not h1 and not h2:
            break
        if not h1:
            cur.next = h2
            h2 = h2.next
        elif not h2:
            cur.next = h1
            h1 = h1.next
        else:
            if h1.data < h2.data:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next

        cur = cur.next

    return merged_list_head

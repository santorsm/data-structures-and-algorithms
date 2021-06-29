from linked_list import LinkedList, Node


def zip_list(first, second):

    first_current = first.head
    second_current = second.head

    while first_current and second_current:

        first_current_next = first_current.next
        second_next = second_current.next

        second_current.next = first_current_next
        first_current.next = second_current

        first_current = first_current_next
        second_current = second_next

    second.head = second_current

    return first

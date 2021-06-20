class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        head_value = self.head

        if head_value == None:
            return False

        while head_value != None:

            if head_value.value != value and head_value.next == None:
                return False
            elif value == head_value.value:
                return True
            elif value != head_value.value:
                head_value = head_value.next

    # def __str__(self, value):
    #     head_value = self.head

    #     if head_value == None:
    #         return "Empty"

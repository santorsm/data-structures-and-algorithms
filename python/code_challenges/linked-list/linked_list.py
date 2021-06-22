class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail_node = None

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

    def __str__(self):

        our_string = ""

        current = self.head

        while current:
            our_string += f"{ {current.value} } -> "
            current = current.next

        our_string += f"None"
        return our_string

    def append(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
            return self

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node

        return self

    def insert_before(self, target, new_value):

        new_node = Node(new_value)

        if self.head is None:
            return None

        if self.head.value == target:
            new_node.next = self.head
            self.head = new_node
            return self

        current = self.head

        while current is not None:
            if current.next.value == target:
                new_node.next = current.next
                current.next = new_node
                return self
            current = current.next

        print("Not in the list")

    def insert_after(self, target, new_value):

        new_node = Node(new_value)

        if self.head is None:
            return None

        current = self.head

        while current is not None:
            if current.value == target:
                new_node.next = current.next
                current.next = new_node
                return self
            current = current.next

        print("Not in the list")

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail_node = None

    def length_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def length_recursive(self, value):
        if value is None:
            return 0
        return 1 + self.length_recursive(value.next)

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

    def kth_position(self, k):

        # find the length of the
        length = 0

        if self.head is None:
            return "Not available for an empty linked list"

        if self.next is None:
            return f"List only has one node - {self.head.value}"

        elif k < 0:
            return "Not available for negative integers"

        elif k > self.length:
            return f"Value {k} is beyond the length of the list"

        place_holder = 0
        current_position = self.head
        search_place = self.length - k


if __name__ == "__main__":
    pass

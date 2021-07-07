class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        # node = new Node(value)
        push_node = Node(value)
        # node.next <-- Top
        push_node.next = self.top
        # top <-- Node
        self.top = push_node

    def pop(self):
        if self.is_empty():
            raise Empty("Cannot pop, stack is empty")
        # Node temp <-- top
        node = self.top
        # top <-- top.next
        self.top = self.top.next
        # temp.next <-- null
        # return temp.value
        return node.value

    def is_empty(self):
        if self.top != None:
            return False

        return True

    def peek(self):
        if self.is_empty():
            raise Empty("Cannot peek, stack is empty")

        else:
            return self.top.value


class Queue:
    def __init__(self, node=None):
        self.front = node
        self.rear = node

    def enqueue(self, value):
        #    node = new Node(value)
        node = Node(value)

        if self.is_empty():
            # if queue is empty assign to both front and rear
            self.front = node
            self.rear = node
        #    rear.next <-- node
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        #    temp.next <-- null
        if self.is_empty():
            raise Empty("Cannot dequeue, queue is empty")
        #    Node temp <-- front
        node = self.front
        #    front <-- front.next
        self.front = self.front.next
        #    return temp.value
        return node.value

    def is_empty(self):
        if self.front != None:
            return False

        return True

    def peek(self):
        if self.is_empty():
            raise Empty("Cannot peek, queue is empty")

        else:
            return self.front.value


class Empty(Exception):
    pass

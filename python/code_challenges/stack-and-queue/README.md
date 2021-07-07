# Stacks and Queues

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Challenge

### Stack

[X] Create a Node class that has properties for the value stored in the Node, and a pointer to the next node

[X] Create a `Stack` class that has a `top` property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created

The class should contain the following methods:

`push`
[X] Arguments: value
[X] adds a new node with that value to the top of the stack with an O(1) Time performance

`pop`
[X] Arguments: none
[X] Returns: the value from node from the top of the stack
[X] Removes the node from the top of the stack
[X] Should raise exception when called on empty stack
Documentation for raising exceptions:

    https://pybit.es/guest-pytest-raises.html
    https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest

`peek`
[X] Arguments: none
[X] Returns: Value of the node located at the top of the stack
[X] Should raise exception when called on empty stack
Documentation for raising exceptions:

    https://pybit.es/guest-pytest-raises.html
    https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest

`is empty`
[X] Arguments: none
[X] Returns: Boolean indicating whether or not the stack is empty

### Queue

[X] Create a Queue class that has a front property. It creates an empty Queue when instantiated
[X] This object should be aware of a default empty value assigned to front when the queue is created

The class should contain the following methods:

`enqueue`
[X] Arguments: value
[X] adds a new node with that value to the back of the queue with an O(1) Time performance

`dequeue`
[X] Arguments: none
[X] Returns: the value from node from the front of the queue
[X] Removes the node from the front of the queue
[X] Should raise exception when called on empty queue
Documentation for raising exceptions:

    https://pybit.es/guest-pytest-raises.html
    https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest

`peek`
[X] Arguments: none
[X] Returns: Value of the node located at the front of the queue
[X] Should raise exception when called on empty stack
Documentation for raising exceptions:

    https://pybit.es/guest-pytest-raises.html
    https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest

`is empty`
[X] Arguments: none
[X] Returns: Boolean indicating whether or not the queue is empty

## Tests

[X] Can successfully push onto a stack
[X] Can successfully push multiple values onto a stack
[X] Can successfully pop off the stack
[X] Can successfully empty a stack after multiple pops
[X] Can successfully peek the next item on the stack
[X] Can successfully instantiate an empty stack
[X] Calling pop or peek on empty stack raises exception
[x] Can successfully enqueue into a queue
[X] Can successfully enqueue multiple values into a queue
[] Can successfully dequeue out of a queue the expected value
[X] Can successfully peek into a queue, seeing the expected value
[X] Can successfully empty a queue after multiple dequeues
[X] Can successfully instantiate an empty queue
[X] Calling dequeue or peek on empty queue raises exception

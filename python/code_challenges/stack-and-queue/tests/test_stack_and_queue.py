from stack_and_queue import __version__
import pytest
from stack_and_queue.stack_and_que import Empty, Stack, Queue


def test_version():
    assert __version__ == "0.1.0"


def test_push_onto_stack():
    s = Stack()
    s.push(1)
    actual = s.top.value
    expected = 1
    assert actual == expected


def test_push_multiple_values_onto_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    actual = s.top.value
    expected = 3
    assert actual == expected


def test_pop_off_the_stack():
    s = Stack()
    s.push(1)
    actual = s.pop()
    expected = 1
    assert actual == expected


def test_empty_stack_after_multiple_pops():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


def test_pop_empty_stack():
    s = Stack()

    with pytest.raises(Empty) as e:
        s.pop()

    assert str(e.value) == "Cannot pop, stack is empty"


def test_peek_to_next_item():
    s = Stack()
    s.push(0)
    s.push(1)
    actual = s.peek()
    expected = 1
    assert actual == expected


def test_instantiate_an_empty_stack():
    s = Stack()
    actual = s.is_empty()
    expected = True
    assert actual == expected


def test_peek_empty_stack():
    s = Stack()

    with pytest.raises(Empty) as e:
        s.peek()

    assert str(e.value) == "Cannot peek, stack is empty"


def test_enqueue():
    q = Queue()
    q.enqueue(0)
    actual = q.front.value
    expected = 0
    assert actual == expected


def test_enqueue_multiple_values_into_a_queue():
    q = Queue()
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    actual = q.front.value
    expected = 3
    assert actual == expected


def test_dequeue_out_of_a_queue_the_expected_value():
    q = Queue()
    q.enqueue(1)
    actual = q.dequeue()
    expected = 1
    assert actual == expected


def test_peek_into_a_queue_seeing_the_expected_value():
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    actual = q.peek()
    expected = 0
    assert actual == expected


def test_empty_a_queue_after_multiple_dequeues():
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


def test_instantiate_an_empty_queue():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


def test_dequeue_or_peek_on_empty_queue_raises_exception():
    q = Queue()

    with pytest.raises(Empty) as error:
        q.peek()

    assert str(error.value) == "Cannot peek, queue is empty"


def test_dequeue_on_empty_queue_raises_exception():
    q = Queue()

    with pytest.raises(Empty) as error:
        q.dequeue()

    assert str(error.value) == "Cannot dequeue, queue is empty"

from linked_list import Node, LinkedList


def test_import():
    assert LinkedList


def test_import_node():
    assert Node


def test_node_instance():
    node = Node("a", None)
    actual = node.value
    expected = "a"
    assert actual == expected
    assert node.next == None


def test_two_nodes():
    node3 = Node("c", None)
    node2 = Node("b", node3)
    node1 = Node("a", node2)

    actual = node2.next.value
    expected = "c"
    assert actual == expected


def test_empty_ll():
    ll = LinkedList()
    assert ll


def test_return_true_for_existing_in_list():
    in_ll = LinkedList()
    in_ll.insert("are")
    in_ll.insert("you")
    in_ll.insert("there")
    actual = in_ll.includes("there")
    expected = True
    assert actual == expected


def test_return_false_for_not_in_list():
    not_in_ll = LinkedList()
    not_in_ll.insert("are")
    not_in_ll.insert("you")
    not_in_ll.insert("there")
    actual = not_in_ll.includes("not")
    expected = False
    assert actual == expected

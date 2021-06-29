from linked_list import Node, LinkedList
from ll_zip import zip_list


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


def test_string():
    append_ll = LinkedList()
    append_ll.insert("a")
    append_ll.insert("b")
    append_ll.insert("c")
    append_ll.append("d")
    actual = str(append_ll)

    expected = "{'c'} -> {'b'} -> {'a'} -> {'d'} -> None"
    assert actual == expected


def test_append():
    append_ll = LinkedList()
    append_ll.insert("a")
    append_ll.insert("b")
    append_ll.insert("c")
    append_ll.append("d")
    actual = str(append_ll)

    expected = "{'c'} -> {'b'} -> {'a'} -> {'d'} -> None"
    assert actual == expected


def test_append_multiple():
    append_ll = LinkedList()
    append_ll.insert("a")
    append_ll.insert("b")
    append_ll.insert("c")
    append_ll.append("d")
    append_ll.append("e")
    actual = str(append_ll)

    expected = "{'c'} -> {'b'} -> {'a'} -> {'d'} -> {'e'} -> None"
    assert actual == expected


def test_can_succesfully_add_a_node_to_the_end_of_the_list():
    ll1 = LinkedList()
    ll1.insert("a")
    ll1.insert("b")
    ll1.insert("c")
    ll1.insert("d")
    ll1.append("Z")
    expected = ["d", "c", "b", "a", "Z"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_can_sucessfully_add_multiple_nodes_to_the_end_of_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    expected = ["a", "b", "c", "d"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_can_succesfully_insert_a_node_before_a_node_in_middle_of_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_before("c", "Z")
    expected = ["a", "b", "Z", "c", "d"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_can_succesfully_insert_a_node_before_the_first_node_of_a_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_before("a", "Z")
    expected = ["Z", "a", "b", "c", "d"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_Can_successfully_insert_after_a_node_in_the_middle_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_after("b", "Z")
    expected = ["a", "b", "Z", "c", "d"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_Can_successfully_insert_a_node_after_the_last_node_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_after("d", "Z")
    expected = ["a", "b", "c", "d", "Z"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_ll_length():
    ll1_length = LinkedList()
    ll1_length = ll1_length.append("a")
    ll1_length = ll1_length.append("b")
    ll1_length = ll1_length.append("c")
    expected = 3
    actual = ll1_length.length_iterative()
    assert actual == expected


# def test_k_negative_integer():
#     ll1 = LinkedList()
#     ll1.append(1).append(2).append(3).append(4)
#     actual = ll1.kth_position(-1)
#     expected = "Not available for negative integers"
#     assert actual == expected


# def test_length_of_one():
#     ll1 = LinkedList()
#     ll1.insert(2)
#     actual = ll1.kth_position(0)
#     expected = "List only has one node - 1"
#     assert actual == expected


# def test_kth_value_at_0():
#     ll3_k = LinkedList()
#     ll3_k = ll3_k.append(2)
#     ll3_k = ll3_k.append(8)
#     ll3_k = ll3_k.append(3)
#     ll3_k = ll3_k.append(1)
#     actual = ll3_k.kth_from_the_end(0)
#     expected = 1
#     assert actual == expected


# def test_kth_value_exceeds_length():
#     ll1 = LinkedList()
#     ll1.append(2)
#     ll1.append(8)
#     ll1.append(3)
#     ll1.append(1)
#     actual = ll1.kth_position(4)
#     expected = "Value 4 is beyond the length of the list"
#     assert actual == expected


def test_seventeen():
    # new_list_one = LinkedList(Node(1,Node(3, Node(5))))
    # new_list_two = LinkedList(Node(2,Node(4, Node(6))))
    new_list_one = LinkedList()
    new_list_two = LinkedList()
    new_list_one.append(1).append(3).append(5)
    new_list_two.append(2).append(4).append(6)
    actual = zip_list(new_list_one, new_list_two)
    # expected = "{1} ->{2} ->{3} ->{4} ->{5} ->{6} -> None "
    expected = "{1} -> {2} -> {3} -> {4} -> {5} -> {6} -> None"
    assert str(actual) == expected

import sys


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        cur = self
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()


def split_list(head):
    end_finder = head
    middle_finder = head

    while end_finder and end_finder.next:
        middle_finder = middle_finder.next
        end_finder = end_finder.next.next

    middle = middle_finder.next
    middle_finder.next = None

    return head, middle


def reverse(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def merge(first, second):
    result = first
    head = first
    first = first.next

    while second:
        result.next = second
        result = result.next
        second = second.next
        if first:
            first, second = second, first

    return head


def create_list(values_list):
    try:
        head = Node(int(values_list[0]))
        cur = head
        for val in values_list[1:]:
            cur.next = Node(int(val))
            cur = cur.next
    except Exception as e:
        print('Incorrect argument. Use python task4.py <int> [<int> ...]')
        head = None
    return head


def reorder_list(head):
    first, second = split_list(head)
    second = reverse(second)
    result = merge(first, second)

    return result


lst = create_list(sys.argv[1:])
if lst is not None:
    reorder_list(lst).print()

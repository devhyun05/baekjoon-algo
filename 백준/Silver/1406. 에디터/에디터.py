import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.current = self.head
            return

        new_node = Node(data)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next

    def cursor_append(self, data):
        if self.current is not None:
            if self.current == self.head:
                new_node = Node(data)
                new_node.next = self.current
                self.current.prev = new_node
                self.head = new_node
            else:
                prev_node = self.current.prev
                new_node = Node(data)
                new_node.prev = prev_node
                new_node.next = self.current
                prev_node.next = new_node
                self.current.prev = new_node

    def move_left(self):
        if self.current is not None and self.current is not self.head:
            self.current = self.current.prev

    def move_right(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next

    def print_nodes_as_list(self):
        res = []
        if self.head is not None:
            curr = self.head
            while curr:
                if curr.data != "":
                    res.append(curr.data)
                curr = curr.next
        return res

    def delete_cursor_left(self):
        if self.current is not None and self.current is not self.head:
            prev_node = self.current.prev

            if prev_node.prev:
                prev_prev_node = prev_node.prev
                prev_prev_node.next = self.current
                self.current.prev = prev_prev_node
            else:
                self.head = self.current
                self.current.prev = None

li = LinkedList()
input_data = input().rstrip()

for c in input_data:
    li.append(c)
li.append("")

m = int(input())

for _ in range(m):
    commands = input().split()
    command = commands[0]

    if command == "P":
        li.cursor_append(commands[1])
    elif command == "L":
        li.move_left()
    elif command == "D":
        li.move_right()
    elif command == "B":
        li.delete_cursor_left()

print("".join(li.print_nodes_as_list()))
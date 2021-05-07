class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        return "[]"

    def add_to_start(self, x):
        '''add x to the left of the list making it the head'''
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        # turn list to [5->4->3->2->1]
        if self.head == None: # if list is empty, return nothing
            return
        elif current.next == None: # if end node
            self.tail = self.head # assign tail to the head to flip
            current.next = previous
            self.head = current #assign current node (last node) to the head
        else:
            next = current.next # head.next is 2
            current.next = previous
            self.reverse_list_recur(next, current)
        

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()
# print(my_list)
my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)
# print(my_list)

my_list.reverse_list_recur(my_list.head, None) #my_list.head = current, previous = None for tracking
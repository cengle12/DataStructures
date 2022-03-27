

class Node:
    """
    A node object used to store data and reference other node objects.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f'Value: {self.value}\nNext: {self.next}'

    def __repr__(self):
        return f'Value: {self.value}\
        Next: {self.next}'


class NodeStack:
    """
    A simple stack object for storing a set of node objects. Data is accessed, inserted, and deleted from one end of the 
    stack uni-directionally.
    """
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.length > 0:
            return f'Head: {self.head.value}\nLength: {self.length}'
        
        else:
            return 'Empty'

    def __repr__(self):
        contents = []
        if self.length > 0:
            curr_node = self.head
            while curr_node:
                contents.append(curr_node.value)
                curr_node = curr_node.next

            return f'Head -> {str(contents)}\
            Length: {self.length}'

        else:
            return 'Empty'

    def isEmpty(self):
        if self.length < 0:  # if the stack somehow has negative length, resets the stack to an empty one of length 0.
            self.head = None
            self.length = 0
            raise Exception("The length of the stack was negative. The stack has been reset.")
        else:
            return self.length == 0

    def push(self, new_value):
        new_node = Node(new_value)  # creates new new to add onto stack
        if self.isEmpty():  # if it's empty we only need to update the head
            self.head = new_node
        else:
            new_node.next = self.head  # update next value of new node to current head
            self.head = new_node  # update head of stack to new node
        self.length += 1

    def peek(self):
        if not self.isEmpty():
            return self.head.value
        else:
            return None

    def pop(self):
        if not self.isEmpty():
            data = self.head.value
            self.head = self.head.next  # changes head to node second from top
            self.length -= 1
            return data
        else:
            raise Exception("The stack is already empty")

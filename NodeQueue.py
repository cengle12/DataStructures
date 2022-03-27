class Node:
    """
    A node object used to store data and reference other node objects.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Value: {self.value}\nNext: {self.next}\nPrevious: {self.prev}'

    def __repr__(self):
        return f'Value: {self.value}\
        Next: {self.next}\
        Previous: {self.prev}'


class NodeQueue:
    """
    A Queue object used to store elements in a First-In-First-Out order. The object uses a singly-linked list of nodes
    and has references to the front and back positions of the list. Additionally, the length of the list is tracked for
    reference.
    """
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def __str__(self):
        if self.length > 0:
            return f'Front: {self.front.value}\nBack: {self.back.value}\nLength: {self.length}'

        else:
            return 'Empty'

    def __repr__(self):
        contents = []
        if self.length > 0:
            curr_node = self.back
            while curr_node:
                contents.append(curr_node.value)
                curr_node = curr_node.next

            return f'Back -> {str(contents)} -> Front\
            Length: {self.length}'

        else:
            return 'Empty'

    def isempty(self):
        if self.length < 0:  # Error checking.
            self.front = None
            self.back = None
            self.length = 0
            raise Exception("The length of the stack was negative. The stack has been reset.")
        else:
            return self.length == 0

    def enqueue(self, value):
        """
        Adds a Node object with a specified value to the back of the queue.
        :param value: Value contained within node that is being stored in the queue.
        """
        new_node = Node(value)

        if self.isempty():
            self.front = new_node
            self.back = new_node

        else:
            new_node.next = self.back
            self.back.prev = new_node
            self.back = new_node

        self.length += 1

    def dequeue(self):
        """
        Removes the Node object at the front of the queue and returns the value stored within it. The next Node in the
        Queue is promoted to the front and the value stored within the removed node is returned.
        :return: Value stored in Node object at the front of the Queue.
        """
        if self.isempty():
            raise Exception('Queue is already empty')

        elif self.length == 1:
            temp = self.front
            self.front = None
            self.back = None
            self.length -= 1

            return temp.value

        else:
            temp = self.front
            self.front = self.front.prev
            self.front.next = None
            self.length -= 1

            return temp.value

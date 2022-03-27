class Node:
    """
    A simple class for Node objects which store any value and are arranged in a doubly-linked list arrangement.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    """
    Double ended list of of Node objects with can be referenced from either end and maintains length as items are added
    or removed.
    """
    def __init__(self):
        self.left = None
        self.right = None
        self.length = 0

    def isempty(self):
        if self.length < 0:  # if the deque somehow has negative length, resets the deque to an empty one of length 0.
            self.left = None
            self.right = None
            self.length = 0
            raise Exception("The length of the deque was negative. The deque has been reset.")
        else:
            return self.length == 0

    def display(self):
        """
        Displays the values contained within each node in the Dequeue.
        """
        if self.isempty():
            print('The deque is currently empty')

        else:
            curr_node = self.left
            return_string = str(curr_node.value)
            while curr_node.next:
                curr_node = curr_node.next
                return_string += '     ' + str(curr_node.value)
            print(return_string)

    def insert_left(self, value):
        """
        Inserts a new node containing a specified value to the left end of the Dequeue. Increments the length of the
        Dequeue by one.
        :param value: Desired value/object being stored in the Node.
        """

        new_node = Node(value)

        if self.isempty():  # If deque is empty, insert and set to left and right
            self.left = new_node
            self.right = new_node

        else:
            new_node.next = self.left
            self.left = new_node
            self.left.next.prev = self.left

        self.length += 1

    def insert_right(self, value):
        """
        Inserts a new node containing a specified value to the right end of the Dequeue. Increments the length of the
        Dequeue by one.
        :param value: Desired value/object being stored in the Node.
        """

        new_node = Node(value)

        if self.isempty():  # If deque is empty, insert and set to right and left
            self.left = new_node
            self.right = new_node

        else:
            new_node.prev = self.right
            self.right = new_node
            self.right.prev.next = self.right

        self.length += 1

    def delete_left(self):
        """
        Removes the leftmost Node object from the Dequeue and returns the value contained within it. Decrements the
        length of the list by one.
        :return: Value contained within the leftmost node.
        """
        if self.isempty():
            return 'Deque is empty, there is nothing to delete'

        elif self.length == 1:
            temp = self.left
            self.left = None
            self.right = None
            self.length -= 1

        else:
            temp = self.left
            self.left = self.left.next
            self.left.prev = None
            self.length -= 1

        return temp.value

    def delete_right(self):
        """
        Deletes the rightmost Node object from the Dequeue and returns the value contained within it. Decrements the
        length of the list by one.
        :return: Value contained within the rightmost node.
        """
        if self.isempty():
            return 'Deque is empty, there is nothing to delete'

        elif self.length == 1:
            temp = self.right
            self.left = None
            self.right = None
            self.length -= 1

        else:
            temp = self.right
            self.right = self.right.prev
            self.right.next = None
            self.length -= 1

        return temp.value

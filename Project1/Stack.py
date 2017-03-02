class Node(object):

    __next = None
    __value = None

    def __init__(self, value=None ):
        self.__value = value
        self.__next = None

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next

class LinkedList(object):
    """ The List itself
    """

    def __init__(self, node=None):
        self.__first = node

    # def __init__(self, node):
    #     self.__first = node

    def head(self):
        return self.__first

    def add_head(self, node):
        node.set_next(self.head())
        self.__first = node

    def remove_head(self):
        self.__first = self.__first.get_next()

    def __repr__(self):
        result = ""
        current = self.head()
        while not (current is None):
            result += " -> " + str(current)
            current = current.get_next()
        return result


class Stack:
    def __init__(self):
        self.__list = LinkedList()  # empty linked list
        self.__topPointer = Node()
        self.__size = 0

    def isEmpty(self):
        return self.__list == 0

    def push(self, e):
        elem = Node(e)
        self.__list.add_head(elem)
        self.__topPointer = elem
        self.__size += 1
        # new_node = Node(value)
        # new_node.set_next(self.__topPointer)
        # self.__topPointer = new_node

    def pop(self):
        self.__size -= 1
        return self.__list.remove_head()

    def size(self):
        return self.__size

    def __repr__(self):
        return self.__list.__repr__()


s = Stack()
s.push("Hello")
s.push(776)
s.push("muli difel")
s.pop()
print (s.isEmpty())
print(s)
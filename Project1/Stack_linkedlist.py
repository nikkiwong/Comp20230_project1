class Node(object):

    __next = None
    __value = None

    def __init__(self, value=None ):
        self.__value = value
        self.__next = None

    def __getitem__(self, index):
        return self.__value[index]

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next

    def get_value(self):
        return self.__value

    def __repr__(self):
        return str(self.get_value())
        # return "node: " + str(self.get_value())

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

    def getNth(self, index):
        current = self.__first  # Initialise temp
        if current == None:
            return []
        else:
            count = 0  # Index of current node
            # Loop while end of linked list is not reached
            while (current):
                if (count == index):
                    result = current
                    print(result)
                    return result
                count += 1
                current = current.get_next()
            return self.__first


class Stack:
    def __init__(self):
        self.__list = LinkedList()  # empty linked list
        self.__topPointer = Node()
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0

    def push(self, e):
        self.elem = Node(e)
        self.__list.add_head(self.elem)
        self.__topPointer = self.elem
        self.__size += 1
        # new_node = Node(value)
        # new_node.set_next(self.__topPointer)
        # self.__topPointer = new_node

    def pop(self):
        if self.__size == 0:
            self.__list = None
            return []
        else:
            self.__size -= 1
            return self.__list.remove_head()

    def size(self):
        return self.__size

    def __repr__(self):
        return self.__list.__repr__()

    def top(self):
        if self.__size == 0:
            return []
        else:
            return self.__list.head()

    def peek(self):
        #peeks at the 2nd node in the linked list
        return self.__list.getNth(1)


# s = Stack()
# s.push([0, 7])
#
# s.push("Go North")
# s.push("Go north")
# s.push("go NOrth")
# s.pop() # ater you pop, you mark the cell to show you've been there?
# s.push("go east")
# s.push("go east")
# s.pop()
# s.push("go south")
# s.push("go south")
# s.push("go south")
# s.push("go south")
# s.pop()
# s.pop()
# # s.pop()
# # s.pop()
# # s.pop()
# # s.pop()
# # s.pop()
# # s.pop()
# #
# print(s.top())
#
# # s.pop()
# print (s.isEmpty())
# print(s)
# print(s.peek())
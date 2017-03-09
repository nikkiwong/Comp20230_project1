class Node(object):
    """ A Node in a Linked List
    """
    __next = None
    __element = None
    
    
    def __init__(self, element=None):
        self.__next = None
        self.__element = element
    
    def get_next(self):
        return self.__next

    def get_element(self):
        return self.__element

    def set_next(self, next):
        self.__next = next

    def set_element(self, element):
        self.__element = element

    def __repr__(self):
        return "node: " + str(self.get_element())


class LinkedList(object):
    """ The List itself
    """

    def __init__(self, node=None):
        self.__first = node

    # def __init__(self, node):
    #     self.__first = node

    def head(self):
        return self.__first

    def add_tail(self, node):
        current = self.head()
        while not current.get_next() == None:
#             if current.get_next() == None:
#                 current.set_next(node)
            current = current.get_next()
        current.set_next(node)

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

        # Returns data at given index in linked list
    def getNth(self, index):
        current = self.__first  # Initialise temp
        print(current)
        count = 0  # Index of current node
        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                result = current
                print(result)
                return result
            count += 1
            current = current.get_next()
        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert (False)
        return 0

# Tests    
l = LinkedList()
l.add_head(Node("toto"))
l.add_head(Node(2))
l.add_tail(Node(9))
l.add_tail(Node(67))
l.add_head(Node("head"))
l.add_tail(Node("tail"))
print(l)
nth = l.getNth(4)

print(nth)

#if you add to the stack then the first element is at the bottom.. but you always have the head pointer at the top element in the stack. and then pop by removing the head element.
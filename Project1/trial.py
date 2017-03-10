class Node(object):
    __next = None
    __element = None

    def __init__(self, element=None):
        self.__element = element
        self.__next = None

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


class Stack(object):
    def __init__(self):
        self.LL = LinkedList()

    def isEmpty(self):
        return self.LL.head() == None

    def push(self, node):
        return self.LL.add_head(node)

    def pop(self):
        if not self.isEmpty():
            return self.LL.remove_head(self)

    def peek(self):
        return self.LL.head(self)


s = Stack()
s.push("hello")
s.push("there")
s.push("you")
s.push("good")
s.push("thing")
print(s.size)
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
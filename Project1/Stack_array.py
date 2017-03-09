class Stack:
    def __init__(self):
        self.__size = 0
        self.__array = []

    def isEmpty(self):
        return self.__array == None

    def push(self, e):
        self.__size += 1
        self.__array += [e]


    def pop(self):
        if self.__size == 1:
            temp = self.__array[0]
            self.__array = []
            self.__size = 0
            return temp
        else:
            temp = self.__array[-1]
            self.__array = self.__array[0:self.__size-1]
            self.__size-=1
            return temp

    def size(self):
        return self.__size

    def top(self):
        if self.__array == []:
            return []
        else:
            return self.__array[self.__size-1]

    def __repr__(self):
        return self.__array.__repr__()
#
# s = Stack()
# s.push("GO north")
#
# s.push("Go North")
# s.push("Go north")
# s.push("go NOrth")
# s.pop() # ater you pop, you mark the cell to show you've been there?
# s.push("go east")
# s.push("go east")
# s.pop()
# s.pop()
# s.push("go south")
# s.push("go south")
# s.push("go south")
# s.push("go south")
# s.pop()
#
# s.pop()
# s.pop()
#
# print(s.top())
# # s.pop()
# print (s.isEmpty())
# print(s)
# print(s.pop())
# print (s)
# print(s.top())
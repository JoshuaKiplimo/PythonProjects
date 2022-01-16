#implementation of a stacks

#A stack follows the LAST IN FIRST OUT PRINCIPLE,
# LIKE A STACK OF BOOKS


class Stack(object):

    def __init__ (self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):#Removes items from the rear
        return self.items.pop()
    def peek(self):#returns top item in the list. last that was put in last
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# s = Stack()

# print(s.IsEmpty())

# s.push(2)
# s.push(3)
# s.push('joshua')

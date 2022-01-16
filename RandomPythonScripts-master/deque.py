#A deque is a data structure where data can be added and removed from both the front and the back.
#It is an improvement of stacks and queues

#NOTE, the FRONT IS THE END OF THE LIST, REAR IS AT THE ZERO INDEXS


Class Deque(object):
    def__init__(self):
        self.items = []
    def addRear(self,item):
        self.items.insert(0,item):#insert item at position 0
            return item
    def addFront(self,item):#add items from the rear
            self.items.append(item)
            return item
    def removeRear(self):#remove items from the front
            popped = self.items.pop(0)
            return popped
    def removeFront(self):#remove items from the end
        rearPopped = self.items.pop()
        return rearPopped

    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

my_deque = Deque()

my_deque.addFront('1')
my_deque.addFront('Hello')

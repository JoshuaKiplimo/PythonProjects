#A queue follows the first in first out principle, first to get in goes out FIRST
#Like a queue of people in a line

class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, item):#Add an item at the last position
        self.items.append(item)
        return item
    def dequeue(self):#removes front item from the queue
        pop = self.items.pop(0)
        return pop
    def IsEmpty(self):
        return len(self.items) ==0
    def size(self):
        return len(self.items)


# q = Queue()
# print(q.enqueue(4))

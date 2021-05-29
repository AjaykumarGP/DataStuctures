


#Queue implementation - Abstract Data Type (ADT)

class QueueOperation():
    def __init__(self, queueSize):
        self.queue = [0 for i in range(10)]
        self.queueSize = queueSize
        self.front = -1
        self.end = -1

    def isFull(self):
        
        if (self.end + 1) % self.queueSize == self.front:
            return True
        return False
    
    def enqueue(self, element):
        if self.isFull():
            print("Queue overloaded!!!")
            return
        elif self.front == -1 and self.end == -1:
            self.front += 1
            self.end += 1
        else:
            self.end = (self.end + 1) % self.queueSize
        
        self.queue[self.end] = element
        return
    
    def isEmpty(self):
        if self.front == -1 and self.end == -1:
            return True
        return False

    def dequeue(self):
        if self.isEmpty():
            print("Queue underflow!!!")
            return
        elif self.front == self.end:
            self.front -= 1
            self.end -= 1
        else:
            self.front = (self.front + 1) % self.queueSize

    
    def printQueue(self):
        print(self.queue)



queueObj = QueueOperation(10)
queueObj.enqueue(1)
queueObj.enqueue(2)
queueObj.enqueue(3)
queueObj.enqueue(4)
queueObj.enqueue(5)
queueObj.enqueue(6)
queueObj.enqueue(7)
queueObj.enqueue(8)
queueObj.enqueue(9)
queueObj.enqueue(10)

queueObj.dequeue()
queueObj.enqueue(11)


print(queueObj.front)
print(queueObj.end)
queueObj.printQueue()


print(queueObj.front)
print(queueObj.end)






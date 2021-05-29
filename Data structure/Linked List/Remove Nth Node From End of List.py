




class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def pushData(self, newData):
        newNode = Node(newData)
        
        temp = self.head
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def findAndRemoveNthNode(self, n):
        counter = 0
        pointerOne = self.head
        pointerTwo = self.head
        previousNode = 0
        
        while(pointerTwo):
            if counter > n-1:
                previousNode = pointerOne
                pointerOne = pointerOne.next
            pointerTwo = pointerTwo.next
            counter += 1
            
        previousNode.next = pointerOne.next
        
        
            
llist = LinkedList()
llist.pushData(1)
llist.pushData(2)
llist.pushData(3)
llist.pushData(4)
llist.pushData(5)
n = 2

llist.findAndRemoveNthNode(n)

llist.printLinkedList()













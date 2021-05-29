



class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedListOne():
    def __init__(self):
        self.head = None
        self.Tail = None
        
    def pushData(self, newData):
        newNode = Node(newData)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    def printLinkedList(self, head):
        temp = head
        while(temp):
            print(temp.data)
            temp = temp.next
            
class LinkedListTwo(LinkedListOne):
    def __init__(self):
        self.head = None
        self.tail = None
        # LinkedListOne.__init__()
        
    def pushData(self, newData):
        newNode = Node(newData)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    def findIntersectionPoint(self, llistA, llistB):
        print("Entering")
        tempOne = llistA
        tempTwo = llistB
        llistOneLoopCounter = 0
        llistTwoLoopCounter = 0
        
        while(tempOne != tempTwo):
            if tempOne != None:
                tempOne = tempOne.next
            else:
                tempOne = llistB
                
            if tempTwo != None:
                tempTwo = tempTwo.next
            else:
                tempTwo = llistA
                
        if tempOne == None and tempTwo == None:
            print("No intersection")
        
        
        
llist = LinkedListOne()
llist.pushData(4)
llist.pushData(1)
llist.pushData(8)
llist.pushData(4)
llist.pushData(5)

llistTwo = LinkedListTwo()
llistTwo.pushData(5)
llistTwo.pushData(6)
llistTwo.pushData(7)
llistTwo.pushData(8)

# llistTwo.head.next.next = llist.head.next.next

llistTwo.findIntersectionPoint(llist.head, llistTwo.head)


llist.printLinkedList(llist.head)
print("----------------------")
llistTwo.printLinkedList(llistTwo.head)





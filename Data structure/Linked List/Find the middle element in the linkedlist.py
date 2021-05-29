

# Find the middle of a given linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.lengthCounter = 0

    def printLinkedList(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
    
    def pushData(self, newData):
        newNode = Node(newData)

        temp = self.head
        #Check if head node is empty
        if self.head == None:
            self.head = newNode
            return

        #Else, traverse till the last node of the list
        while(temp.next != None):
            temp = temp.next

        temp.next = newNode

    def findMiddleElement(self):

        singlePointer = self.head
        doublePointer = self.head

        while( doublePointer != None and doublePointer.next != None):  
            
            #Single unit traverse
            singlePointer = singlePointer.next

            #Double unit traverse
            temp = doublePointer.next
            doublePointer = temp.next 

        
        print(singlePointer.data)
    


llist = LinkedList()
llist.pushData(10)
llist.pushData(20)
llist.pushData(30)
llist.pushData(40)
llist.pushData(50)
llist.pushData(60)



llist.findMiddleElement()

llist.printLinkedList()



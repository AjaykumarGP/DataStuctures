

# Detect loop in a linked list
#Using Floyd cycle algorithm

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.occuranceCounter = 0

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

    def detectLoop(self):

        firstPointer = self.head
        secondPointer = self.head

        while(firstPointer and secondPointer and secondPointer.next):

            firstPointer = firstPointer.next
            secondPointer = secondPointer.next.next

            if firstPointer == secondPointer:
                print("Loop exist")
                return

        print("Loop does not exist")
        
    

llist = LinkedList()
llist.pushData(20)
llist.pushData(4)
llist.pushData(15)
llist.pushData(10)

#Creating a loop for testing

llist.head.next.next.next.next = llist.head

llist.detectLoop()

# llist.printLinkedList()



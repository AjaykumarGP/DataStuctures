


# Find Length of a Linked List (Iterative and Recursive)
#Iterative

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

    def getLength(self):
        lengthCounter = 0

        temp = self.head
        while(temp):
            lengthCounter += 1
            temp = temp.next

        # print("Length of the list: ", lengthCounter)

    def recursiveLengthCounter(self, temp):
        if temp.next != None:
            self.recursiveLengthCounter(temp.next)
        self.lengthCounter += 1

    def getLengthByRecursive(self):
        temp = self.head
        if self.head == None:
            print("No elements in the list")
        else:
            self.recursiveLengthCounter(temp)
            print("Length of the list: ", self.lengthCounter)


llist = LinkedList()
llist.pushData(10)
llist.pushData(20)
llist.pushData(30)
llist.pushData(40)
llist.pushData(50)
llist.pushData(60)


llist.getLength()
llist.getLengthByRecursive()
llist.printLinkedList()





# Program for n’th node from the end of a Linked List


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
    
    def findElement(self, searchIndex):
        
        counter = 1
    
        secondPointer = 0

        temp = self.head
        secondTemp = self.head

        while(temp != None):
            if secondPointer >= searchIndex:
                secondTemp = secondTemp.next
                
            secondPointer+= 1
            temp = temp.next

        print("Element: ", secondTemp.data)


llist = LinkedList()
llist.pushData(35)
llist.pushData(15)
llist.pushData(4)
llist.pushData(20)


llist.findElement(3)

llist.printLinkedList()



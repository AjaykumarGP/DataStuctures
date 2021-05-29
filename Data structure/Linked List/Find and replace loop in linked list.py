

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
                return secondPointer

        return -1
        
    def getLastNodeFromFullLoop(self, secondPointer):
        temp = secondPointer
        while(temp.next != self.head):
            temp = temp.next
        return temp
        
    def removeLoop(self, secondPointer):
        count = 0
        temp = self.head
        previousPointer = secondPointer
        
        while(temp and secondPointer):
            if temp == secondPointer:
                print("Loop start from: ", secondPointer.data)
                if secondPointer == self.head:
                    return self.getLastNodeFromFullLoop(secondPointer)
                else:
                    return previousPointer
            
            temp = temp.next
            previousPointer = secondPointer
            secondPointer = secondPointer.next
            
    def straightenList(self, lastNode):
        print("Linked list deprived from loop")
        lastNode.next = None
            

    def detectAndRemoveLoop(self):
        result = self.detectLoop()
        if(result == -1):
            print("No loop exist")
        else:
            lastNode = self.removeLoop(result)
            self.straightenList(lastNode)
            
        

        

llist = LinkedList()
llist.pushData(20)
llist.pushData(4)
llist.pushData(15)
llist.pushData(10)
llist.pushData(25)

#Creating a loop for testing
# print(llist.head.next.next.next.next.next)
llist.head.next.next.next.next.next = llist.head.next.next.next.next

llist.detectAndRemoveLoop()

llist.printLinkedList()

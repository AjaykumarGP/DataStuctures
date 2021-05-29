

# Add two numbers represented by linked lists | Set 1

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

    def addTwoLinkedList(self, llistOne, llistTwo):
        pointerOne = llistOne
        pointerTwo = llistTwo
        remainder = 0

        while(pointerOne or pointerTwo or remainder > 0):
            
            if pointerOne != None:
                firstOperand = pointerOne.data
                pointerOne = pointerOne.next
            else:
                firstOperand = 0
            
            if pointerTwo != None:
                secondOperand = pointerTwo.data
                pointerTwo = pointerTwo.next
            else:
                secondOperand = 0

            newValue = firstOperand + secondOperand + remainder

            if newValue >= 10:
                splitedValue = newValue % 10
                remainder = int(newValue / 10)
                self.pushData(splitedValue)
            else:
                remainder = 0
                self.pushData(newValue)

            
            
    

llist = LinkedList()
llist.pushData(2)
llist.pushData(4)
llist.pushData(3)
llist.pushData(8)


llistTwo = LinkedList()
llistTwo.pushData(5)
llistTwo.pushData(6)
llistTwo.pushData(7)
llistTwo.pushData(9)


#Resultant llist
llistResult = LinkedList()
llistResult.addTwoLinkedList(llist.head, llistTwo.head)

llist.printLinkedList()
print("---------")
llistTwo.printLinkedList()
print("---------")
llistResult.printLinkedList()

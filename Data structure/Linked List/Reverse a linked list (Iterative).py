

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

    def reverseList(self):
        previousNode = None
        currentNode = self.head
        nextNode = self.head.next

       
        while(currentNode):
            if currentNode.next == None:
                self.head = currentNode
                currentNode.next = previousNode
                break

            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next


llist = LinkedList()
llist.pushData(1)
llist.pushData(2)
llist.pushData(3)
llist.pushData(4)

llist.reverseList()

llist.printLinkedList()

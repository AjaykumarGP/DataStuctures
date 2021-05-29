


# Search an element in a Linked List (Iterative and Recursive)
#Recursively

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

    def findDataRecursively(self, temp, searchKey):

        if temp != None and temp.data == searchKey:
            return 1

        elif temp != None:
            if temp.next == None:
                return -1
            return self.findDataRecursively(temp.next, searchKey)
            

    def searchElement(self, searchKey):
        temp = self.head
        result = self.findDataRecursively(temp, searchKey)
        if result == -1:
            print("Element not found in the list")
        elif result == 1:
            print("Element found in the list")

llist = LinkedList()
llist.pushData(10)
llist.pushData(20)
llist.pushData(30)
llist.pushData(40)
llist.pushData(50)
llist.pushData(90)

llist.searchElement(10)



llist.printLinkedList()



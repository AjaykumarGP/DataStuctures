


# Search an element in a Linked List (Iterative and Recursive)
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

    def searchElement(self, searchKey):
        temp = self.head

        while(temp):
            if temp.data == searchKey:
                print("Element found")
                return
            temp = temp.next

        print("Element not found")

    


llist = LinkedList()
llist.pushData(10)
llist.pushData(20)
llist.pushData(30)
llist.pushData(40)
llist.pushData(50)
llist.pushData(60)

llist.searchElement(70)



llist.printLinkedList()


